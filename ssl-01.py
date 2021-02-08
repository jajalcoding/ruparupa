import ssl
import socket
import pprint
import sys

try :
    HOSTNAME=sys.argv[1]
except:
    HOSTNAME='www.google.com'

CMD = "GET / HTTP/1.1\r\nHost:"+HOSTNAME+"\r\nUser-Agent : Mozilla Firefox 5.0\r\nAccept:*/*\r\n\r\n"

ctx = ssl.create_default_context()

ctx.check_hostname = False
ctx.hostname_checks_common_name = False
f = open('tmpcert.der','wb')
cert = ctx.get_ca_certs(binary_form=True)
f.write(cert)
f.close()
ctx.load_verify_locations('tmpcert.der')

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
hasil=wrapsock.recv(2048)

print(hasil)