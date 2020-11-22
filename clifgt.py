from paramiko import SSHClient, AutoAddPolicy
import sys

def ssh_fgt(ipadd,portno,user,pwd,command):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect(ipadd,username=user,password=pwd,port=portno)
    print ("Executing :"+command)
    stdin, stdout, stderr = client.exec_command(command)
# use decode to translate b' and \n
    print(stdout.read().decode())
    client.close()

fgtuser="testing"
fgtpass="12345"
fgtip="192.168.1.99"

perintah=sys.argv[1:]

if not perintah:
    print("Must have a command to execute in 3 fgt !")
    exit()

strperintah = ' '.join(perintah)
print(strperintah)
ssh_fgt(fgtip, 22, fgtuser, fgtpass, strperintah )
