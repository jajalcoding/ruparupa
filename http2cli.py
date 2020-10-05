# http2cli v 1.0
# by TAS AthionXX
# very useful for ssh command that needs password
# with additional handler and loop if not succesful will wait 5 seconds

# Usage :
# python http2cli http://a.a.a.a/value.txt http://a.a.a.a/config-template.txt
# 
# sample content of config-template.txt :
#
# config firewall policy
# edit 1
# set name {{ namanya }}
# end
# 
# sample content of value.txt :
# host : "192.168.1.99"
# username : "admin"
# password : "password"
# namanya : "FortigateRumah"
# 
# Expected result :
# fgt in ip 192.168.1.99 with user admin and password password will be configured with
#  
# config firewall policy
# edit 1
# set name FortigateRumah
# end
# 

from paramiko import SSHClient, AutoAddPolicy
from paramiko.auth_handler import AuthenticationException, SSHException
from jinja2 import Template
import string
import time
import sys
import socket
import requests
import yaml
import pdb


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

def ambilconfig(urlfile):
    # no errorhandling for now, assumed will have result !
    teks = requests.get(urlfile)
    return teks.text

def prepareconfig(urlconfigdata,urlconfigtemplate,namafile):
    # confdata harus return data dict
    teks = ambilconfig(sys.argv[1])
    confdata = yaml.load(teks, Loader=yaml.FullLoader)
    print(confdata)

    # conftemplate hanya text
    conftemplate = ambilconfig(sys.argv[2])

    # proses jinja2 change
    #pdb.set_trace()

    j2_template = Template( conftemplate )
    conffinal = j2_template.render( confdata )

    # write file belum !
    #print(conffinal)
    f = open(namafile, "w")
    f.write(conffinal)
    f.close()

    try:
        return confdata['host'], confdata['username'], confdata['password']
    except:
        return '', '', ''


def main():
    if len(sys.argv) < 2:
        # Requires fgt ip and password
        print ("Must have 2 parameter : configdata configtemplate" )
        print ("python http2cli.py http://1.1.1.1/configdata.txt http://1.1.1.1/configtemplate.txt")
        exit()

    hostname, username, passw = prepareconfig(sys.argv[1], sys.argv[2], 'conftemp.txt' )

    if ( hostname == '' or username == '' or passw == '' ):
        print("Wrong config file, must have host, username, password ...")
        exit()

    waittime = 5
    result = False
    s = time.perf_counter()
    
    while ( result==False ):
        result = ssh_cli_command(hostname,username,passw,'conftemp.txt')
        if ( result==False ):
            print ("Can not connect to "+hostname+", will retry in "+str(waittime)+" seconds.....")
            print ("Or press Ctrl+C to break !!")
            time.sleep(waittime)
    
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


if __name__ == '__main__':
   main()
