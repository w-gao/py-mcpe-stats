import struct


class Packet:
    """
    A class encapsulating the contents of a single network packet to be sent or
    received through the network. The self.buffer bytes object is the actual
    contents of the packet, where helper methods such as the read_*() and
    write_*() can be used to encode and decode the contents.
    """
    def __init__(self):
        self.offset = 0
        self.buffer = b''

    def encode(self) -> None:
        pass

    def decode(self) -> None:
        self.offset = 0

    def read(self, length) -> bytes:
        """ Read the given length number of bytes from the buffer."""
        if length < 0:
            self.offset = len(self.buffer) - 1
            return bytes(0)

        buff = bytearray()
        for i in range(length):
            self.offset += 1
            buff.append(self.buffer[self.offset])
        return buff

    def read_byte(self):
        self.offset += 1
        return self.buffer[self.offset]

    def read_short(self):
        return struct.unpack(">H", self.read(2))[0]

    def read_triad(self):
        return struct.unpack('>i', self.read(3) + b'\x00')[0]

    def read_int(self):
        return struct.unpack(">i", self.read(4))[0]

    def read_long(self):
        return struct.unpack(">q", self.read(8))[0]

    def read_string(self) -> str:
        length = self.read_short()
        return self.read(length).decode('utf-8')

    def write(self, val: bytes) -> None:
        """ Write bytes to the buffer."""
        self.buffer += val

    def write_byte(self, val):
        self.buffer += val

    def write_short(self, val):
        self.buffer += struct.pack('>h', val)

    def write_triad(self, val):
        self.buffer += struct.pack('>i', val)[:3]

    def write_int(self, val):
        self.buffer += struct.pack('>i', val)

    def write_long(self, val):
        self.buffer += struct.pack('>q', val)

    def write_string(self, val):
        if not isinstance(val, bytes):
            val = val.encode('utf-8')
        self.write_short(len(val))
        self.buffer += val
