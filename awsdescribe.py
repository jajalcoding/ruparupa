import boto3
import pprint
import yaml
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

secretdata = loadyaml2dict('awskey.cfg')

ec2 = boto3.client('ec2',
                   'us-east-1',
                   aws_access_key_id=secretdata['key'],
                   aws_secret_access_key=secretdata['secret'])

response = ec2.describe_instances() 

for m in response['Reservations']:
    cetak = "Instance-Id: "+m['Instances'][0]['InstanceId']+' ' 
    try:
        cetak = cetak+m['Instances'][0]['Tags'][3]['Value']+' '
    except:
        cetak = cetak+'NO TAG'+' '
    cetak = cetak + "Private :"+m['Instances'][0]['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['PrivateIpAddress']
    try :
        cetak = cetak + " --> public IP :"+m['Instances'][0]['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['Association']['PublicIp']
    except :
        cetak = cetak + " - no public IP !"
    cetak = cetak + " >> Status: "+m['Instances'][0]['State']['Name']
    print(cetak)
    hsl=findtagvalue(m['Instances'][0]['Tags'],'aws:autoscaling:groupName')
    print(hsl)
    hsl=findtagvalue(m['Instances'][0]['Tags'],'Name')
    print(hsl)
    print('-----------------------------------------------------')
#pprint.pprint(response)











'''
(Pdb) pprint.pprint(response['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['Association']['PublicIp'])
'184.72.210.60'
(Pdb) pprint.pprint(response['Reservations'][0]['Instances'][0]['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['PrivateIpAddress'])
'10.0.0.11'

(Pdb) pprint.pprint(response['Reservations'][5])
{'Groups': [],
 'Instances': [{'AmiLaunchIndex': 1,
                'Architecture': 'x86_64',
                'BlockDeviceMappings': [{'DeviceName': '/dev/sda1',
                                         'Ebs': {'AttachTime': datetime.datetime(2020, 11, 25, 2, 46, 2, tzinfo=tzutc()),
                                                 'DeleteOnTermination': True,
                                                 'Status': 'attached',
                                                 'VolumeId': 'vol-0845acfe2297b4dcd'}},
                                        {'DeviceName': '/dev/sdb',
                                         'Ebs': {'AttachTime': datetime.datetime(2020, 11, 25, 2, 46, 2, tzinfo=tzutc()),
                                                 'DeleteOnTermination': True,
                                                 'Status': 'attached',
                                                 'VolumeId': 'vol-0fd91382c0072913e'}}],
                'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'},
                'ClientToken': 'bd45d7f5-2c70-03ed-1f01-cfa5b58ce081',
                'CpuOptions': {'CoreCount': 2, 'ThreadsPerCore': 2},
                'EbsOptimized': False,
                'EnaSupport': True,
                'EnclaveOptions': {'Enabled': False},
                'HibernationOptions': {'Configured': False},
                'Hypervisor': 'xen',
                'IamInstanceProfile': {'Arn': 'arn:aws:iam::123534227893:instance-profile/fgt-auto-tgw-mixed-StackMainWorkload-1KRH640ZX0KAR-FgtInstanceProfile-QMPYEM4MK9UH',
                                       'Id': 'AIPARZQZWXG2YCB5OXQ2V'},
                'ImageId': 'ami-0642e5e1fd6c0b2e7',
                'InstanceId': 'i-04f70afb6491b4770',
                'InstanceType': 'm4.xlarge',
                'KeyName': 'fgt_virginia',
                'LaunchTime': datetime.datetime(2020, 11, 25, 2, 46, 1, tzinfo=tzutc()),
                'MetadataOptions': {'HttpEndpoint': 'enabled',
                                    'HttpPutResponseHopLimit': 1,
                                    'HttpTokens': 'optional',
                                    'State': 'applied'},
                'Monitoring': {'State': 'disabled'},
                'NetworkInterfaces': [{'Association': {'IpOwnerId': 'amazon',
                                                       'PublicDnsName': '',
                                                       'PublicIp': '3.236.153.74'},
                                       'Attachment': {'AttachTime': datetime.datetime(2020, 11, 25, 2, 46, 1, tzinfo=tzutc()),
                                                      'AttachmentId': 'eni-attach-0db94ef9983b86cdf',
                                                      'DeleteOnTermination': True,
                                                      'DeviceIndex': 0,
                                                      'NetworkCardIndex': 0,
                                                      'Status': 'attached'},
                                       'Description': '',
                                       'Groups': [{'GroupId': 'sg-0579dfc597c9b5d7e',
                                                   'GroupName': 'web-server'}],
                                       'InterfaceType': 'interface',
                                       'Ipv6Addresses': [],
                                       'MacAddress': '02:25:02:a3:fa:35',
                                       'NetworkInterfaceId': 'eni-0f28ae96f205d644f',
                                       'OwnerId': '123534227893',
                                       'PrivateIpAddress': '10.100.1.241',
                                       'PrivateIpAddresses': [{'Association': {'IpOwnerId': 'amazon',
                                                                               'PublicDnsName': '',
                                                                               'PublicIp': '3.236.153.74'},
                                                               'Primary': True,
                                                               'PrivateIpAddress': '10.100.1.241'}],
                                       'SourceDestCheck': True,
                                       'Status': 'in-use',
                                       'SubnetId': 'subnet-031a8b447e7c6973d',
                                       'VpcId': 'vpc-0e44c5f87607f6db4'}],
                'Placement': {'AvailabilityZone': 'us-east-1a',
                              'GroupName': '',
                              'Tenancy': 'default'},
                'PrivateDnsName': 'ip-10-100-1-241.ec2.internal',
                'PrivateIpAddress': '10.100.1.241',
                'ProductCodes': [{'ProductCodeId': '9y27bf3bfjm4inhuawvzrrmq1',
                                  'ProductCodeType': 'marketplace'}],
                'PublicDnsName': '',
                'PublicIpAddress': '3.236.153.74',
                'RootDeviceName': '/dev/sda1',
                'RootDeviceType': 'ebs',
                'SecurityGroups': [{'GroupId': 'sg-0579dfc597c9b5d7e',
                                    'GroupName': 'web-server'}],
                'SourceDestCheck': True,
                'State': {'Code': 16, 'Name': 'running'},
                'StateTransitionReason': '',
                'SubnetId': 'subnet-031a8b447e7c6973d',
                'Tags': [{'Key': 'aws:ec2launchtemplate:id',
                          'Value': 'lt-026e089fcad729805'},
                         {'Key': 'aws:autoscaling:groupName',
                          'Value': 'FortADC-ASG'},
                         {'Key': 'Name', 'Value': 'FAD-ASG'},
                         {'Key': 'aws:ec2launchtemplate:version', 'Value': '5'},
                         {'Key': 'project', 'Value': 'FAD-ASG'}],
                'VirtualizationType': 'hvm',
                'VpcId': 'vpc-0e44c5f87607f6db4'},
               {'AmiLaunchIndex': 0,
                'Architecture': 'x86_64',
                'BlockDeviceMappings': [{'DeviceName': '/dev/sda1',
                                         'Ebs': {'AttachTime': datetime.datetime(2020, 11, 25, 2, 46, 2, tzinfo=tzutc()),
                                                 'DeleteOnTermination': True,
                                                 'Status': 'attached',
                                                 'VolumeId': 'vol-08a494d8f0efa43be'}},
                                        {'DeviceName': '/dev/sdb',
                                         'Ebs': {'AttachTime': datetime.datetime(2020, 11, 25, 2, 46, 2, tzinfo=tzutc()),
                                                 'DeleteOnTermination': True,
                                                 'Status': 'attached',
                                                 'VolumeId': 'vol-0a2dcd0527f40676d'}}],
                'CapacityReservationSpecification': {'CapacityReservationPreference': 'open'},
                'ClientToken': 'bd45d7f5-2c70-03ed-1f01-cfa5b58ce081',
                'CpuOptions': {'CoreCount': 2, 'ThreadsPerCore': 2},
                'EbsOptimized': False,
                'EnaSupport': True,
                'EnclaveOptions': {'Enabled': False},
                'HibernationOptions': {'Configured': False},
                'Hypervisor': 'xen',
                'IamInstanceProfile': {'Arn': 'arn:aws:iam::123534227893:instance-profile/fgt-auto-tgw-mixed-StackMainWorkload-1KRH640ZX0KAR-FgtInstanceProfile-QMPYEM4MK9UH',
                                       'Id': 'AIPARZQZWXG2YCB5OXQ2V'},
                'ImageId': 'ami-0642e5e1fd6c0b2e7',
                'InstanceId': 'i-0bc6cac413b69e93c',
                'InstanceType': 'm4.xlarge',
                'KeyName': 'fgt_virginia',
                'LaunchTime': datetime.datetime(2020, 11, 25, 2, 46, 1, tzinfo=tzutc()),
                'MetadataOptions': {'HttpEndpoint': 'enabled',
                                    'HttpPutResponseHopLimit': 1,
                                    'HttpTokens': 'optional',
                                    'State': 'applied'},
                'Monitoring': {'State': 'disabled'},
                'NetworkInterfaces': [{'Association': {'IpOwnerId': 'amazon',
                                                       'PublicDnsName': '',
                                                       'PublicIp': '18.209.230.69'},
                                       'Attachment': {'AttachTime': datetime.datetime(2020, 11, 25, 2, 46, 1, tzinfo=tzutc()),
                                                      'AttachmentId': 'eni-attach-0314fac1973ed9a1d',
                                                      'DeleteOnTermination': True,
                                                      'DeviceIndex': 0,
                                                      'NetworkCardIndex': 0,
                                                      'Status': 'attached'},
                                       'Description': '',
                                       'Groups': [{'GroupId': 'sg-0579dfc597c9b5d7e',
                                                   'GroupName': 'web-server'}],
                                       'InterfaceType': 'interface',
                                       'Ipv6Addresses': [],
                                       'MacAddress': '02:66:04:46:72:83',
                                       'NetworkInterfaceId': 'eni-0fad2d9ce7a0e2d56',
                                       'OwnerId': '123534227893',
                                       'PrivateIpAddress': '10.100.1.42',
                                       'PrivateIpAddresses': [{'Association': {'IpOwnerId': 'amazon',
                                                                               'PublicDnsName': '',
                                                                               'PublicIp': '18.209.230.69'},
                                                               'Primary': True,
                                                               'PrivateIpAddress': '10.100.1.42'}],
                                       'SourceDestCheck': True,
                                       'Status': 'in-use',
                                       'SubnetId': 'subnet-031a8b447e7c6973d',
                                       'VpcId': 'vpc-0e44c5f87607f6db4'}],
                'Placement': {'AvailabilityZone': 'us-east-1a',
                              'GroupName': '',
                              'Tenancy': 'default'},
                'PrivateDnsName': 'ip-10-100-1-42.ec2.internal',
                'PrivateIpAddress': '10.100.1.42',
                'ProductCodes': [{'ProductCodeId': '9y27bf3bfjm4inhuawvzrrmq1',
                                  'ProductCodeType': 'marketplace'}],
                'PublicDnsName': '',
                'PublicIpAddress': '18.209.230.69',
                'RootDeviceName': '/dev/sda1',
                'RootDeviceType': 'ebs',
                'SecurityGroups': [{'GroupId': 'sg-0579dfc597c9b5d7e',
                                    'GroupName': 'web-server'}],
                'SourceDestCheck': True,
                'State': {'Code': 16, 'Name': 'running'},
                'StateTransitionReason': '',
                'SubnetId': 'subnet-031a8b447e7c6973d',
                'Tags': [{'Key': 'aws:autoscaling:groupName',
                          'Value': 'FortADC-ASG'},
                         {'Key': 'aws:ec2launchtemplate:id',
                          'Value': 'lt-026e089fcad729805'},
                         {'Key': 'project', 'Value': 'FAD-ASG'},
                         {'Key': 'aws:ec2launchtemplate:version', 'Value': '5'},
                         {'Key': 'Name', 'Value': 'FAD-ASG'}],
                'VirtualizationType': 'hvm',
                'VpcId': 'vpc-0e44c5f87607f6db4'}],
 'OwnerId': '123534227893',
 'RequesterId': '940372691376',
 'ReservationId': 'r-0eef39d42cb2107e0'}
(Pdb)

>>> for m in response['Reservations']:
...     print (m['Instances'][0]['NetworkInterfaces'][0]['PrivateIpAddresses'][0]['PrivateIpAddress'])
...
10.0.0.11
10.100.0.248
10.100.1.189
10.100.1.153
10.100.1.137
10.100.1.241
10.0.10.11
>

(Pdb) response['Reservations'][0]['Instances'][0]['Tags'][0]['Key']
'owner'
(Pdb) response['Reservations'][0]['Instances'][0]['Tags'][0]['Value']
'ISINA'
(Pdb) response['Reservations'][0]['Instances'][0]['Tags'][1]['Key']
'Role'
(Pdb) response['Reservations'][0]['Instances'][0]['Tags'][2]['Key']
'Project'

'''
