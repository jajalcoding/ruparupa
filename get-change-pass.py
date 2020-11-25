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

def findtagvalue(datadict,tagfindstring):
    hasil = []
    for i in datadict:
        if (i['Key']==tagfindstring):
             hasil.append(i['Value'])
    return hasil

def access_ssh(devip, keyfilename):
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
    
    if (hasil.find('New Password')>0):
        remote_shell.send(secretdata['fadpass']+'\n')
        time.sleep(2) # enter confirm password
        remote_shell.send(secretdata['fadpass']+'\n')
        recvstr = remote_shell.recv(1000)
        print(recvstr.decode())
    else:
        print('This device has been changed password before, exiting..')

    client.close()

def get_aws_fad():

    ec2 = boto3.client('ec2',
                   'us-east-1',
                   aws_access_key_id=secretdata['key'],
                   aws_secret_access_key=secretdata['secret'])
    # just filter on running instance
#    response = ec2.describe_instances(Filters=[ { 'Name' : 'instance-state-name', 
#                                                  'Values' : ['running'] 
#                                                } ] )
    response = ec2.describe_instances()
    print("Only with aws:autoscaling:groupName")

    daftarip=[]    
    for m in response['Reservations']:
        hsl=findtagvalue(m['Instances'][0]['Tags'],'aws:autoscaling:groupName')
        if hsl:
           # there is autoscaling group, then most likely > 1 then must loop again
           for i in m['Instances']:
              print("Instance-Id: "+i['InstanceId']+' Private :'+i['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['PrivateIpAddress']+\
                    " --> public IP :"+i['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['Association']['PublicIp']  ) 
              daftarip.append( i['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['Association']['PublicIp'] )
    
    return daftarip

def main():
    # take all list of IP address that have tags aws:autoscaling:groupName
    listid = get_aws_fad()
    print(listid)
    for m in listid:
       print('Accessing '+m)
       access_ssh(m,'fgt_virginia.pem')


if __name__ == "__main__":
    # please put key, secret and new password for fadc in awskey.cfg
    secretdata = loadyaml2dict('awskey.cfg')
    main()
