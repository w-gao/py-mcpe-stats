"""a Python software that gets basic information about an MCPE server

UnconnectedPong class

Copyright (c) 2016 w-gao
"""

from .packet import Packet


class UnconnectedPong(Packet):

    def __init__(self):
        super().__init__()

        self.ping_id = None
        self.server_id = None
        self.server_info = None

    def encode(self):
        pass

    def decode(self):

        self.ping_id = self.read_long()
        self.server_id = self.read_long()

        # Skip Magic
        self.offset += 16

        self.server_info = self.read_string()
