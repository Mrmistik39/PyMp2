"""
 ________         ___    ___      _____ ______           ________
|\   __  \       |\  \  /  /|    |\   _ \  _   \        |\   __  \
\ \  \|\  \      \ \  \/  / /    \ \  \\\__\ \  \       \ \  \|\  \
 \ \   ____\      \ \    / /      \ \  \\|__| \  \       \ \   ____\
  \ \  \___|       \/  /  /        \ \  \    \ \  \       \ \  \___|
   \ \__\        __/  / /           \ \__\    \ \__\       \ \__\
    \|__|       |\___/ /             \|__|     \|__|        \|__|
                \|___|/

    VK: vk.com/ea714867
    TODO доделать raklib, беды с подключением
"""

from src.PyMp.Utils.MainLogger import MainLogger
from src.PyMp.Network.protocol.ProtocolInfo import ProtocolInfo
from src.PyMp.Network.Query.Query import Query
from src.PyMp.Network.raklib.server.PyRakLibServer import PyRakLibServer
from ..PyMp.Utils.Config import Config
import time


class Server(object):

    def __init__(self, start_time):
        self.players = {}
        self.startTime = 0
        self.mainLogger = MainLogger()
        self.mainLogger.start()
        self.mainLogger.Info('Starting server for minecraft PE...')
        version = ', '.join(ProtocolInfo.MINECRAFT_VERSION)
        self.mainLogger.Info(f'Support version: {version}')
        # self.mainLogger.Info('Starting Query from 0.0.0.0:19132') TODO Query
        # self.query = Query('127.0.0.1', 19133)                    TODO Query
        # self.query.query()                                        TODO Query
        self.RakLibServer = PyRakLibServer(19132)
        self.mainLogger.Info(f'Server starting in {(int(time.time()) - start_time)} second')

    def getOnlinePlayers(self):
        return self.players
