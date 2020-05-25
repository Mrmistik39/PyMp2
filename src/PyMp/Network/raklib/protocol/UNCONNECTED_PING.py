"""
PyRakLib networking library.
   This software is not affiliated with RakNet or Jenkins Software LLC.
   This software is a port of PocketMine/RakLib <https://github.com/PocketMine/RakLib>.
   All credit goes to the PocketMine Project (http://pocketmine.net)
 
   Copyright (C) 2015  PyRakLib Project

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from src.PyMp.Network.raklib.PyRakLib import PyRakLib
from src.PyMp.Network.raklib.protocol.Packet import Packet


class UNCONNECTED_PING(Packet):

    PID = 0x01
    pingID = None

    def _encode(self):
        self.putByte(self.PID)
        self.putLong(self.pingID)
        self.put(PyRakLib.MAGIC)

    def _decode(self):
        self.get()
        self.pingID = self.getLong()