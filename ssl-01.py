#!/usr/bin/python3

import ssl
import socket
import pprint
import sys

try :
    HOSTNAME=sys.argv[1]
except:
    HOSTNAME='www.fortinet.com'

CMD = "GET / HTTP/1.1\r\nHost:"+HOSTNAME+"\r\nUser-Agent : Mozilla Firefox 5.0\r\nAccept:*/*\r\n\r\n"

ctx = ssl.create_default_context()

sock = socket.create_connection((HOSTNAME,443))
sock.settimeout(3) 

try:    
    wrapsock = ctx.wrap_socket(sock,server_hostname=HOSTNAME)
except:
# these 3 lines must exist so that certificate error not occcured !
# if got SSL Certificate error, re-set the following to ignore cert
    ctx.check_hostname = False
    ctx.hostname_checks_common_name = False
    ctx.verify_mode=ssl.CERT_NONE
    sock = socket.create_connection((HOSTNAME,443))
    wrapsock = ctx.wrap_socket(sock,server_hostname=HOSTNAME)

print("Available Ciphers:")
pprint.pprint(ctx.get_ciphers()) # list available ciphers

print("Agreed Cipher:")
print(wrapsock.cipher()) # list agreed cipher

cert = wrapsock.getpeercert() # if ssl.CERT_NONE, it will get empty
pprint.pprint(cert)

print(wrapsock.sendall(CMD.encode('ascii')))

while True:    
    try:
        hasil=wrapsock.recv(1024)
    except socket.timeout :
        print("Timeout...")
        break
    if not hasil:
        break
    
    print(hasil)

sock.close()
