"""a Python software that gets basic information about an MCPE server

ServerData class

Copyright (c) 2016 w-gao
"""


class ServerData:

    # Query status
    SUCCESS = False

    # Request info
    PING_ID = -1
    SERVER_ID = -1

    GAME_ID = 'UNKNOWN'
    SERVER_NAME = 'UNKNOWN'
    GAME_PROTOCOL = -1
    GAME_VERSION = 'UNKNOWN'
    NUM_PLAYERS = -1
    MAX_PLAYERS = 1000

    HASH_CODE = -1
    MOTD = ''
    GAMEMODE = ''
