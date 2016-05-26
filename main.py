import argparse
import shlex
import socket
from cfetch import __version__, get_ticker, get_registered_tickers
from cfetch import load_default_plugins
from os.path import expanduser, join, exists
from os import makedirs

__title__ = 'coinserve'
__author__ = 'Justyn Temme'


load_default_plugins()

HOST, PORT = '', 8888
# Set socket up to listen on port 8888
listen_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
# Add the format for the arguments
parser = argparse.ArgumentParser(description='Argparse')
parser.add_argument('-a', '--api', help='uses an API by name')
# parser.add_argument('-k', '--kind', help='specifies which kind of rate to get')
parser.add_argument('amount', default=1, help='amount of the original currency', nargs='?', type=float)
parser.add_argument('src', help='currency from which to convert')
parser.add_argument('dest', help='currency to which to convert')
# Listen on port for connection until user interupt.
while True:
	client_connection, client_address = listen_socket.accept()
	print ('connection recieved')
	request = client_connection.recv(1024).decode()
	if len(request) > 5:# check if request is initial connection request. All real requests should be longer than 5 
		args = parser.parse_args(shlex.split(request))
		# Use the cfetch API to get number based on arguments provided above
		data =('%.8f'%get_ticker(args.api).get_rate(args.src, args.dest, args.amount)).encode()
		print(data)
		client_connection.send(data) #send back the data

client_connection.close()
