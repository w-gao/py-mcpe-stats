#
# Copyright (c) 2016-2021 w-gao
#
import argparse
import logging
import sys
import socket
from contextlib import contextmanager
from random import randint
from typing import Generator

from mcstats.lib.raknet import UnconnectedPing, RakLib, UnconnectedPong

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.WARNING)


class StatsNetworkError(Exception):
    """
    Exception thrown when the socket connection fails.
    """
    pass


class StatsServerData:
    """
    An object encapsulating the data from the target Minecraft: Bedrock edition
    server by retrieving the data sent during the initial steps of the RakNet
    login sequence. This is the information that gets displayed in the server
    list page in game, which includes the motd, player count, etc.
    """

    def __init__(self):
        self.ping_id = -1
        self.server_id = -1

        self.game_id = None
        self.server_name = None
        self.game_protocol = None
        self.game_version = None

        self.num_players = -1
        self.max_players = -1

        self.hash_code = -1
        self.motd = None
        self.gamemode = None

    def __str__(self):
        return "{}({})".format(self.__class__.__name__, ', '.join(f"{k}={repr(v)}" for k, v in self.__dict__.items()))


@contextmanager
def mcstats(host: str, port: int = 19132, timeout: int = 5) -> Generator[StatsServerData, None, None]:
    """
    A context manager to make a socket connection to the target host and port,
    then initiates the first few steps of the RakNet login sequence enough to
    get the response containing the information about the server. The socket
    connection is automatically closed when the context manager exits.
    """
    soc = None

    try:
        logger.debug(f"Connecting to {host}:{port}...")
        soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        soc.settimeout(timeout)
        soc.connect((host, port))

        # send ping
        ping = UnconnectedPing(randint(1, 999999999))
        ping.encode()
        soc.send(ping.buffer)

        # receive pong
        buff = soc.recv(65565)
        if buff[0] is RakLib.UNCONNECTED_PONG:
            pong = UnconnectedPong()
            pong.buffer = buff
            pong.decode()

            stats = _parse_data(pong.server_info)
            stats.ping_id = pong.ping_id
            stats.server_id = pong.server_id

            yield stats
        else:
            raise StatsNetworkError(f"Unconnected pong is not received.")

    except socket.error as msg:
        raise StatsNetworkError(f"Failed to query: '{msg}'")
    finally:
        logger.debug("Closing connection...")
        soc.close()


def _parse_data(raw_data: str) -> StatsServerData:
    """
    Internal function for parsing the raw data from the target server into a
    StatsServerData object.
    """
    data = raw_data.replace(r'\;', '').split(';')  # trim
    stats = StatsServerData()

    if len(data) >= 6:
        stats.game_id = data[0]
        stats.server_name = data[1]
        stats.game_protocol = int(data[2])
        stats.game_version = data[3]
        stats.num_players = int(data[4])
        stats.max_players = int(data[5])

    if len(data) >= 7:
        stats.HASH_CODE = data[6]

    if len(data) >= 9:
        stats.motd = data[7]
        stats.gamemode = data[8]

    return stats


def main(args=None):
    parser = argparse.ArgumentParser(description="")

    parser.add_argument("host", type=str, help="The host of the server.")
    parser.add_argument("-p", "--port", type=int, default=19132, help="The port of the server.")
    parser.add_argument("-t", "--timeout", type=int, default=5, help="The time limit of the socket connection.")
    parser.add_argument("-d", "--debug", action='store_true', help="Enable debug logging.")

    options = parser.parse_args(args)
    if options.debug:
        logging.basicConfig(level=logging.DEBUG)

    host = options.host
    port = options.port
    timeout = options.timeout

    try:
        with mcstats(host, port=port, timeout=timeout) as data:
            def key(k):
                return k.capitalize().replace('_', ' ')

            stdout: str = '\n'.join(f"{key(k)}: {v}" for k, v in data.__dict__.items())
            print(stdout)
    except Exception as e:
        print(f"An error occurred during query: {e}")


if __name__ == "__main__":
    main(sys.argv[1:])
