from src.PyMp.Network.Query.raknet.packet.packet import Packet
from src.PyMp.Network.Query.raknet.raknet import RakLib


class UnconnectedPing(Packet):

    def __init__(self, ping_id):
        super().__init__()

        self.ping_id = ping_id

    def encode(self):
        self.write_byte(bytes([RakLib.UNCONNECTED_PING]))
        self.write_long(self.ping_id)
        self.write(RakLib.MAGIC)
        self.write_long(0)

    def decode(self):
        pass