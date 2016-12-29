import socket
import ServerData

from random import randint
from raknet.RakLib import RakLib
from raknet.packet.UNCONNECTED_PING import UNCONNECTED_PING
from raknet.packet.UNCONNECTED_PONG import UNCONNECTED_PONG


class Query:

    def __init__(self, host, port=19132, timeout=5):
        self.host = host
        self.port = port
        self.timeout = timeout

        self.socket = None

    def query(self):
        # init socket
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
            self.socket.settimeout(self.timeout)

            self.socket.connect((self.host, self.port))
        except socket.error as msg:
            print("Cannot connect to the server. Error: ", msg)
            return None

        # Returned data
        server_data = ServerData.ServerData()

        # get data from the server
        try:
            ping = UNCONNECTED_PING(randint(1, 999999999))
            ping.encode()
            self.socket.send(ping.buffer)

            buff = self.socket.recv(65565)

            if buff[0] is RakLib.UNCONNECTED_PONG:
                pong = UNCONNECTED_PONG()
                pong.buffer = buff
                pong.decode()

                server_data.PING_ID = pong.ping_id
                server_data.SERVER_ID = pong.server_id

                info = pong.server_info.split(';')

                if len(info) == 6:
                    server_data.GAME_ID = info[0]
                    server_data.SERVER_NAME = info[1]
                    server_data.GAME_PROTOCOL = int(info[2])
                    server_data.GAME_VERSION = info[3]
                    server_data.NUM_PLAYERS = int(info[4])
                    server_data.MAX_PLAYERS = int(info[5])

                server_data.SUCCESS = True

        # Perhaps the server is offline
        except socket.error as msg:
            print('Failed to query. Error message: ', msg)

        # print('closing the socket')
        self.socket.close()
        return server_data
