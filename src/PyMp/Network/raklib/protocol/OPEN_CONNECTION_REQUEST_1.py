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


class OPEN_CONNECTION_REQUEST_1(Packet):
    PID = 0x05

    protocol = PyRakLib.PROTOCOL
    mtuSize = None

    def _encode(self):
        self.putByte(self.PID)
        self.put(PyRakLib.MAGIC)
        self.putByte(self.protocol)
        for i in range(0, self.mtuSize - 18):
            self.putByte(0)

    def _decode(self):
        self.get()
        self.get(16)
        self.protocol = self.get()
        self.mtuSize = len(self.get(True)) + 18