class Packet:
    def __init__(self):

        self.offset = 0
        self.buffer = None

    def encode(self):
        pass

    def decode(self):
        self.offset = 0

    def read(self, length):
        if length < 0:
            self.offset = len(self.buffer) - 1
            return bytes(0)

        buff = bytearray()
        for i in range(length):
            self.offset += 1

            if self.offset > len(self.buffer) - 1:
                break

            buff.append(self.buffer[self.offset])
        return buff

    def read_byte(self):
        self.offset += 1
        return self.buffer[self.offset]

    def read_short(self):
        # b = self.read(2)
        # return ((b[0] & 0xFF) << 8) + (b[1] & 0xFF)
        return int.from_bytes(self.read(2), byteorder='big', signed=True)

    def read_triad(self):
        return int.from_bytes(self.read(3), byteorder='big', signed=True)

    def read_int(self):
        return int.from_bytes(self.read(4), byteorder='big', signed=True)

    def read_long(self):
        return int.from_bytes(self.read(8), byteorder='big', signed=True)

    def read_string(self):
        l = self.read_short()
        return self.read(l).decode('utf-8')
