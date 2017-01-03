"""a Python software that gets basic information about an MCPE server

UnconnectedPing class

Copyright (c) 2016 w-gao
"""

from .packet import Packet
from ..rak_lib import RakLib


class UnconnectedPing(Packet):

    def __init__(self, ping_id):
        super().__init__()

        self.ping_id = ping_id

    def encode(self):
        self.write_byte(bytes([RakLib.UNCONNECTED_PING]))
        self.write_long(self.ping_id)
        self.write(RakLib.MAGIC)

        # Guid
        self.write_long(0)

    def decode(self):
        pass
