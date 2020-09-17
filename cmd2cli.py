# cmd2cli v 1.0
# by TAS AthionXX
# very useful for ssh command that needs password
# Usage :
# python cmd2cli.py 192.168.1.99 admin pass1234 fgtcli.txt
# 
# sample content of fgtcli.txt :
#
# config firewall policy
# edit 1
# set name "Rumah2Internet"
# end

from paramiko import SSHClient, AutoAddPolicy
import string
import time
import sys

def ssh_host(ipadd,user,pwd,command):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect(ipadd,username=user,password=pwd)
    stdin, stdout, stderr = client.exec_command(command)

    print(stdout.read())
    client.close()

def ssh_cli_command(ipadd,user,pwd,namafile):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(ipadd,username=user,password=pwd)
    remote_shell = client.invoke_shell()

    f = open(namafile, "r")
    
    for line in f:
        if ( len(line)>1 ):
            remote_shell.send(line.strip()+"\n")
            while not remote_shell.recv_ready():
                time.sleep(.1)
            output = remote_shell.recv(10000)
            print(output.decode("ascii"))
    
    f.close()

    client.close()


def main():
    if len(sys.argv) < 4:
        # Requires fgt ip and password
        print ("Must have 4 parameter : hostname username password commandfile")
        exit()

    hostname = sys.argv[1]
    username = sys.argv[2]
    passw = sys.argv[3]
    namafile = sys.argv[4]

    ssh_cli_command(hostname,username,passw,namafile)

if __name__ == '__main__':
   main()
