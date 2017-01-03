"""a Python software that gets basic information about an MCPE server

RakLib Class

Copyright (c) 2016 w-gao
"""


class RakLib:

    PROTOCOL = 6
    MAGIC = b"\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78"

    UNCONNECTED_PING = 0x01
    UNCONNECTED_PONG = 0x1c
