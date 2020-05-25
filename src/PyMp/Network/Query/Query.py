from ...Utils.Binary import Binary
import hashlib


class Query:
    HANDSHAKE = 9
    STATISTICS = 0

    def __init__(self, logger, port=19132):
        self.logger = logger
        self.logger.Info(f'Query launched on the port {port}')

    def regenerateInfo(self):
        pass

    def regenerateToken(self):
        pass

    def substr(self, text, count):
        return text[count:]

    def hash512(self, text):
        return hashlib.sha512(text.encode()).hexdigest()

    def getTokenString(self, token, salt):
        return Binary.read_int(
            self.hash512(
                str(salt) + ":" + str(token)
            )
            # TODO substr(hash("sha512", $salt . ":" . $token, true), 7, 4)
        )

    


