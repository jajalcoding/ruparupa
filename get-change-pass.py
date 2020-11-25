import boto3
import pprint
import yaml
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
    hasil = remote_shell.recv(500000)
    print(hasil.decode())
    client.close()

def get_aws_fad():
    secretdata = loadyaml2dict('awskey.cfg')

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
           print("Instance-Id: "+m['Instances'][0]['InstanceId']+' Private :'+m['Instances'][0]['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['PrivateIpAddress']+\
                 " --> public IP :"+m['Instances'][0]['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['Association']['PublicIp']  ) 
           daftarip.append( m['Instances'][0]['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['Association']['PublicIp'] )
    return daftarip

def main():
    # take all list of IP address that have tags aws:autoscaling:groupName
    listid = get_aws_fad()
    print(listid)
    for m in listid:
       print('Accessing '+m)
       access_ssh(m,'fgt_virginia.pem')


if __name__ == "__main__":

    main()
