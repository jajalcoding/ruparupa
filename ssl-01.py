#!/usr/bin/python3

import ssl
import socket
import pprint
import sys

try :
    HOSTNAME=sys.argv[1]
except:
    HOSTNAME='192.168.1.99'

CMD = "GET / HTTP/1.1\r\nHost:"+HOSTNAME+"\r\nUser-Agent : Mozilla Firefox 5.0\r\nAccept:*/*\r\n\r\n"

ctx = ssl.create_default_context()

# these 3 lines must exist so that certificate error not occcured !
ctx.check_hostname = False
ctx.hostname_checks_common_name = False
ctx.verify_mode=ssl.CERT_NONE 

sock = socket.create_connection((HOSTNAME,443))
wrapsock = ctx.wrap_socket(sock,server_hostname=HOSTNAME)

print("Available Ciphers:")
pprint.pprint(ctx.get_ciphers()) # list available ciphers
servcert = ctx.get_ca_certs() # get the server certs

print("Agreed Cipher:")
print(wrapsock.cipher()) # list agreed cipher

cert = wrapsock.getpeercert()

pprint.pprint(cert)

print(wrapsock.sendall(CMD.encode('ascii')))

while True:
    hasil=wrapsock.recv(2048)
    if ( len(hasil)<1 ):
        break
    print(hasil)
