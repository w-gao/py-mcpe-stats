"""a Python software that gets basic information about an MCPE server

Packet class

Copyright (c) 2016 w-gao
"""

import struct


class Packet:
    def __init__(self):
        self.offset = 0
        self.buffer = b''

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

    def read_string(self):
        l = self.read_short()
        return self.read(l).decode('utf-8')

    def write(self, val):
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
        b = val.encode('utf-8')
        self.write_short(len(b))
        self.buffer += b
