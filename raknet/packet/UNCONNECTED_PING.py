import struct
from raknet.packet.Packet import Packet
from raknet.RakLib import RakLib


class UNCONNECTED_PING(Packet):

    def __init__(self, ping_id):
        super().__init__()

        self.ping_id = ping_id

    def encode(self):
        self.buffer = RakLib.UNCONNECTED_PING + struct.pack('>q', self.ping_id) + RakLib.MAGIC

    def decode(self):
        pass
