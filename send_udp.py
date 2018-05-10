import socket
import os
import sys
import urllib
import random
import threading


def get_random_ip():
	a = random.randint(10, 220)
	b = random.randint(10, 220)
	c = random.randint(10, 220)
	d = random.randint(10, 220)
	randomip = ".".join([str(x) for x in [a, b, c, d]])
	return randomip

	#randomip = "http://"+randomip
	#return randomip

def send_udp(threadnum):
	i = 0
	while(1):
		i += 1
		UDP_IP = get_random_ip()
		UDP_PORT = 8080
		MESSAGE = "Hello, World!"

		if(i%100000==0): print("IP: {0} Thread: {1}".format(UDP_IP, threadnum))

		#print "UDP target IP:", UDP_IP
		#print "UDP target port:", UDP_PORT
		#print "message:", MESSAGE

		sock = socket.socket(socket.AF_INET, # Internet
		             socket.SOCK_DGRAM) # UDP
		sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
		sock.close()


numthreads = 4

for i in range(0, numthreads):
	threading.Thread(target=send_udp, args=(i,)).start()

#send_udp()