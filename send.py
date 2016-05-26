##
##  coinserve - Socket wrapper for coinfetch api
##  Copyright (C) 2016 Justyn Temme
##
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, version 3 only.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU Affero General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost' 
port = 8888
sock.connect((host,port))
message = "-a btce 1 btc usd"
sock.sendall(message.encode())
data = sock.recv(1024).decode()
print (data)
sock.close()
