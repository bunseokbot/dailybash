import subprocess
import random
import time
import glob

lastfile = ""

def send_slackmsg(filename, message):
	s = subprocess.Popen(['/bin/bash', 'dailybash.sh', filename, message], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = s.communicate()
	del s

def get_randomimage(lastfile):
	iList = glob.glob('image/*.*')
	random.shuffle(iList)
	if len(lastfile) != 0:
		iList.remove(lastfile)

	return iList[0]

def write_msg(fname, msg):
	f = open(fname, 'a+')
	f.write(msg + "\n")
	f.close()

def dailybash_main():
	global lastmsg, lastfile
	msg = "#dailybash"
	fname = get_randomimage(lastfile)
	curtime = int(time.time())
	send_slackmsg(fname, msg)
	lastmsg = msg

	wmsg = "[%d] Filename : %s [Success]" %(curtime, fname)
	print(wmsg)
	write_msg('dailybash_history.log', wmsg)

while True:
	try:
		dailybash_main()
	except Exception as e:
		print("[*] Dailybash have a exception :(")
		write_msg('dailybash_error.log', str(e))
	finally:
		time.sleep(3600*8)
