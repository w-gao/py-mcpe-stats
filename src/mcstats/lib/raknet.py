from mcstats.lib.packet import Packet


class RakLib:
    """
    A class encapsulating the constant values of RakLib.
    """
    PROTOCOL = 6
    MAGIC = b"\x00\xff\xff\x00\xfe\xfe\xfe\xfe\xfd\xfd\xfd\xfd\x12\x34\x56\x78"

    UNCONNECTED_PING = 0x01
    UNCONNECTED_PONG = 0x1c


class UnconnectedPing(Packet):
    """
    Represent an unconnected ping packet. C -> S.
    """
    def __init__(self, ping_id):
        super(UnconnectedPing, self).__init__()
        self.ping_id = ping_id

    def encode(self) -> None:
        self.write_byte(bytes([RakLib.UNCONNECTED_PING]))
        self.write_long(self.ping_id)
        self.write(RakLib.MAGIC)

        self.write_long(0)  # guid

    def decode(self) -> None:
        pass


class UnconnectedPong(Packet):
    """
    Represent an unconnected pong packet. S -> C.
    """
    def __init__(self):
        super(UnconnectedPong, self).__init__()

        self.ping_id = None
        self.server_id = None
        self.server_info = None

    def encode(self) -> None:
        pass

    def decode(self) -> None:
        self.ping_id = self.read_long()
        self.server_id = self.read_long()
        self.offset += 16  # skip magic

        self.server_info = self.read_string()
