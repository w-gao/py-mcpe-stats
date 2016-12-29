from raknet.packet.Packet import Packet
from raknet.RakLib import RakLib


class UnconnectedPing(Packet):

    def __init__(self, ping_id):
        super().__init__()

        self.ping_id = ping_id

    def encode(self):

        self.write_byte(RakLib.UNCONNECTED_PING)
        self.write_long(self.ping_id)
        self.write(RakLib.MAGIC)

        # Guid
        self.write_long(0)

    def decode(self):
        pass
