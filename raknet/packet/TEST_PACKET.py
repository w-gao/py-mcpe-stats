from raknet.packet.Packet import Packet


class Test(Packet):

    def encode(self):

        self.write_byte(b'\x01')
        self.write_long(0)
        self.write(bytes(16))
        self.write_long(0)

        self.write_byte(b'\x01')
        self.write_short(12345)
        self.write_triad(5322)
        self.write_int(2453)
        self.write_long(421089)
        self.write_string('test,\nhi')

    def decode(self):
        pass
