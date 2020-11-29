import boto3
import yaml
import time
from paramiko import SSHClient, AutoAddPolicy
from paramiko.auth_handler import AuthenticationException, SSHException

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

def lambda_handler(event, context):

    # TODO implement
    print(event)

    if (event['detail-type']!='EC2 Instance Launch Successful'):
        print('exiting lambda function.. only for EC2 Instance Launch')
        return {
            'statusCode': 200,
            'body': "Not EC2 Instance Launch"
            }


    asgname = 'FortADC-ASG'
    # getting all the required file from s3 bucket
    # actually awskey.cfg at this moment only hold fad password, aws key and aws secret keys is not used in lambda
    print('downloading s3')
    s3_client = boto3.client('s3')
    s3_client.download_file('ateguh-lambda', 'fgt_virginia.pem', '/tmp/private.key')
    s3_client.download_file('ateguh-lambda','awskey.cfg','/tmp/awskey.cfg')
    s3_client.download_file('ateguh-lambda','awscombined.cfg','/tmp/awscombined.cfg')

    secretdata = loadyaml2dict('/tmp/awskey.cfg')

    # need to get the instanceid that AutoScalingGroup launch and get the ip address for ssh
    ec2id = event['detail']['EC2InstanceId']

    if (event['detail']['AutoScalingGroupName']!=asgname):
        print('Autoscaling Group Name is not correct, exiting')
        return {
                'statusCode': 404,
                'body': "Error"
            }

    ec2 = boto3.resource('ec2',region_name='us-east-1')

    current = list(ec2.instances.filter(InstanceIds=[ ec2id ]))
    print(ec2id+' has public ip:'+current[0].public_ip_address+' and private ip:'+current[0].private_ip_address)
    
    devip = current[0].public_ip_address
    devprivateip = current[0].private_ip_address

    # execute the ssh with 2 phase : 1) change password 2) inject script from awscombined.cfg

    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    print('Waiting for 60 seconds to make sure unit boot up....')
    time.sleep(60)

    print('SSH Client try to connect to '+devip)
    try:
        client.connect(devip, username='admin',port=22, timeout=10, key_filename='/tmp/private.key')
    except:
        print('Error connecting ....')
        return {
                'statusCode': 404,
                'body': "Error"
            }

    remote_shell = client.invoke_shell()
    recvstr = remote_shell.recv(1000)
    hasil = recvstr.decode()

    if (hasil.find('New Password')>0):

        # change password
        remote_shell.send(secretdata['fadpass']+'\n')
        time.sleep(2) # enter confirm password
        remote_shell.send(secretdata['fadpass']+'\n')
        recvstr = remote_shell.recv(1000)
        print(recvstr.decode())
        time.sleep(2) # wait 2 seconds before firing the configuration
        injectconfig = loadconfig ('/tmp/awscombined.cfg')

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

        print(ec2id+" with "+devip+' has been configured with new password and injected with config')
        print('-'*50)
    else:
        print('This device has been changed password before, exiting..')

    client.close()

    return {
        'statusCode': 200,
        'body': "Success inject script"
    }


