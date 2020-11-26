'''
This module will do the following - it will use file awskey.cfg, that contains key,secret,etc.
1. Find aws instance running with tag aws:autoscaling:groupName
2. For each of them do :
    a. ssh using private key provided fgt_virginia.pem
    b. if the device answer with "New Password", it will do
        1) change with new password
        2) config the device with file
    c. DONE

'''
import boto3
import pprint
import yaml
import time
from paramiko import SSHClient, AutoAddPolicy
from paramiko.auth_handler import AuthenticationException, SSHException
import pdb

def loadyaml2dict(namafile):
    try:
        f = open(namafile, "r")
    except:
        print(namafile+" can not be opened!")
        exit()

    sentdata = yaml.load(f, Loader=yaml.FullLoader)
    f.close()
    return sentdata

def loadconfig(namafile):
    try:
        f = open(namafile, "r")
    except:
        print(namafile+" can not be opened!")
        exit()

    sentdata = f.readlines()
    f.close()
    return sentdata


def findtagvalue(datadict,tagfindstring):
    hasil = []
    for i in datadict:
        if (i['Key']==tagfindstring):
             hasil.append(i['Value'])
    return hasil

def access_ssh(devip, keyfilename, devprivateip):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    try:
        client.connect(devip, username='admin',port=22, timeout=10, key_filename=keyfilename)
    except:
        print('Error connecting ....')
        exit()

    remote_shell = client.invoke_shell()
    recvstr = remote_shell.recv(1000)
    hasil = recvstr.decode()
    print(hasil)
    # if there is 'New Password', it means this is a new FADC, will need to change the pass, otherwise it means it is already not first-time setup
    # if this is a new FADC, then config it from secretdata['fadinitconfig'] file
    # the issue is... we must change the ip address
    # and only in config virtual server ( any other part can not be changed !!)
    if (hasil.find('New Password')>0):

        remote_shell.send(secretdata['fadpass']+'\n')
        time.sleep(2) # enter confirm password
        remote_shell.send(secretdata['fadpass']+'\n')
        recvstr = remote_shell.recv(1000)
        print(recvstr.decode())
        time.sleep(2) # wait 2 seconds before firing the configuration
        injectconfig = loadconfig (secretdata['fadinitconfig'])

        modulenow = ''
        for lines in injectconfig:
            if ( lines.find('config ')==0 ):
                modulenow = lines

            # need to replace if there is ip address -> devprivateip - but only if it is under virtual server !
            if (lines.find('set ip ')>0 and ( modulenow=='config load-balance virtual-server\n') ):
               sentlines = 'set ip '+devprivateip+'\n'
               print('** changing ip address to '+devprivateip)
            else:
                sentlines = lines

            remote_shell.send(sentlines)
            time.sleep(0.1)
            recvstr = remote_shell.recv(1000)
            print(recvstr.decode())

        print(devip+' has been configured with new password and injected with config from '+secretdata['fadinitconfig'])
        print('-'*50)
    else:
        print('This device has been changed password before, exiting..')

    client.close()

def get_aws_fad():

    ec2 = boto3.client('ec2',
                   'us-east-1',
                   aws_access_key_id=secretdata['key'],
                   aws_secret_access_key=secretdata['secret'])
    # just filter on running instance
    response = ec2.describe_instances(Filters=[ { 'Name' : 'instance-state-name', 
                                                'Values' : ['running'] 
                                               } ] )

    print("Only with aws:autoscaling:groupName")

    daftarip=[]    
    for m in response['Reservations']:
        hsl=findtagvalue(m['Instances'][0]['Tags'],'aws:autoscaling:groupName')
        if hsl:
           # there is autoscaling group, then most likely > 1 then must loop again
           for i in m['Instances']:

              print("Instance-Id: "+i['InstanceId']+' Private :'+i['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['PrivateIpAddress']+\
                    " --> public IP :"+i['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['Association']['PublicIp']  ) 

              daftarip.append({
                   'public':i['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['Association']['PublicIp'], 
                   'private':i['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['PrivateIpAddress']          
                })
    
    return daftarip

def main():
    # take all list of IP address that have tags aws:autoscaling:groupName
    listid = get_aws_fad()
    print(listid)
    for m in listid:
       print('Accessing '+m['public'])
       access_ssh(m['public'],'fgt_virginia.pem',m['private'])


if __name__ == "__main__":
    # please put key, secret and new password for fadc in awskey.cfg
    secretdata = loadyaml2dict('awskey.cfg')
    main()


'''
>>> a.append({'old':'1.1.1.1','new':'2.2.2.2'})
>>> a
[{'old': '1.1.1.1', 'new': '2.2.2.2'}]
>>> [0]
[0]
>>> a[0]
{'old': '1.1.1.1', 'new': '2.2.2.2'}
>>> a[0]['old']
'1.1.1.1'
>>> a[0]['new']
'2.2.2.2'
>>> a.append({'old':'3.3.3.3','new':'4.4.4.4'})
>>> a
[{'old': '1.1.1.1', 'new': '2.2.2.2'}, {'old': '3.3.3.3', 'new': '4.4.4.4'}]
>>> a[1]
{'old': '3.3.3.3', 'new': '4.4.4.4'}
>>> 
'''
