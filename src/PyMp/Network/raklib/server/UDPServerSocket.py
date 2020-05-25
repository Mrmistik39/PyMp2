import logging
import socket


class UDPServerSocket:

    logger = None
    socket = None

    def __init__(self, port: int = 19132, interface: str = "0.0.0.0"):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        try:
            self.socket.bind((interface, port))
        except Exception as e:
            print("FAILED TO BIND TO PORT! Perhaps another server is running on the port?")
            print(str(e))
        finally:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            self.socket.setblocking(False)

    def close(self):
        self.socket.close()

    def readPacket(self):
        try:
            data = self.socket.recvfrom(65535)
            # print("Packet IN: "+str(data))
            return data
        except Exception as e:
            pass

    def writePacket(self, buffer, dest, port):
        # print("Packet OUT: "+str(buffer))
        return self.socket.sendto(buffer, (dest, port))

