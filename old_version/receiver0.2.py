from bit import *
import sys
import time
from scapy.all import *

def get_bit(ip):
	#time.sleep(int(time.time()/2+1)*2-time.time())
	#time.sleep(1)
	#if (int(time.time()/10)*10+5-time.time())<=0:
         #       time.sleep(int(time.time()/10+1)*10-time.time())
        #else:
        #        time.sleep(int(time.time()/10+1)*10-5-time.time())
	#time.sleep(int(time.time())+1-time.time())
	time.sleep((int(time.time()*10)/2+1)*2/10.0-time.time())
	global pre_id
	packet=sr1(IP(dst=ip)/ICMP())
	differ=0
	temp=pre_id
	pre_id=packet[0][0].id
	print "IPID",pre_id
	if (packet[0][0].id-1)<temp:
		differ=packet[0][0].id+65535-temp
	else:
		differ=packet[0][0].id-1-temp
	if(differ>=4):
		print "Get Bit 1 successfully at %s" %(time.time())
		return 1
	else:
		print "Get Bit 0 successfully at %s" %(time.time())
		return 0

if __name__=="__main__":
	conf.verb=0
	pre_id=0
	ip=raw_input("Type in the ip you wanna receive message from:")
	print "Receiving message......."
	bit=get_bit(ip)
	bits=[]
	flag=0
	char=[]
	while True:
		bit=get_bit(ip)
		if bit==1:
			flag=flag+1
		else:
			flag=0
		if flag==3:
			break
	while True:
		for i in range(8):
			bit=get_bit(ip)
			bits.append(bit)
			if i==2 and bits[0]==1 and bits[1]==1 and bits[2]==1:
				break
		if len(bits)==3:
			break
		print bits
		print frombits(bits)
		char.append(frombits(bits))
		bits=[]
	print " "
	print "The message you have received is "+''.join(char)
