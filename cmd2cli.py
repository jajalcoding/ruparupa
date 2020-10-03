# cmd2cli v 2.0
# by TAS AthionXX
# very useful for ssh command that needs password
# with additional handler and loop if not succesful will wait 5 seconds

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
from paramiko.auth_handler import AuthenticationException, SSHException
import string
import time
import sys
import socket

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
    try:
        client.connect(ipadd,username=user,password=pwd)
        remote_shell = client.invoke_shell()

    except AuthenticationException:
        print("Authentication failed, please verify your credentials !")
        return False
    except SSHException as sshException:
        print("Unable to establish SSH connection: %s" % sshException)
        return False
    except socket.error:
        print("Unable to connect to host "+ipadd)
        return False

    try:
        f = open(namafile, "r")
    except :
        print("File "+namafile+" is not found !")
        return False

    for line in f:
        if ( len(line)>1 ):
            remote_shell.send(line.strip()+"\n")
            while not remote_shell.recv_ready():
                time.sleep(.1)
            output = remote_shell.recv(10000)
            print(output.decode("ascii"))
    
    f.close()

    client.close()
    return True

def main():
    if len(sys.argv) < 4:
        # Requires fgt ip and password
        print ("Must have 4 parameter : hostname username password commandfile")
        exit()

    hostname = sys.argv[1]
    username = sys.argv[2]
    passw = sys.argv[3]
    namafile = sys.argv[4]
    waittime = 5
    result = False
    s = time.perf_counter()
    
    while ( result==False ):
        result = ssh_cli_command(hostname,username,passw,namafile)
        if ( result==False ):
            print ("Can not connect to "+hostname+", will retry in "+str(waittime)+" seconds.....")
            print ("Or press Ctrl+C to break !!")
            time.sleep(waittime)
    
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


if __name__ == '__main__':
   main()
