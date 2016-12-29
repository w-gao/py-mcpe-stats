import struct
from raknet.packet.Packet import Packet
from raknet.RakLib import RakLib


class UnconnectedPing(Packet):

    def __init__(self, ping_id):
        super().__init__()

        self.ping_id = ping_id

    def encode(self):
        self.buffer = RakLib.UNCONNECTED_PING + struct.pack('>q', self.ping_id) + RakLib.MAGIC + struct.pack(
            '>q', 0)

    def decode(self):
        pass
