'''
requirements.txt 
pip install yaml
pip install paramiko

Usage : get-config.py namafile.yaml

Just make sure file have correct parameter, because we dont do any checking of the value !

namafile.yaml contains :

device:
- ip : '192.168.1.99'
- port : 22
- username : 'testing'
- password : '12345'
- configcmd : 'show'

module :
- system interface
- firewall policy
- firewall ippool
- router ospf

filename : 'combined.cfg'

----- for ssh with private key (aws)

device:
- ip : '192.168.1.99'
- port : 22
- username : 'ec2-user'
- privatekeyfile : 'xxxx.pem'

'''
from paramiko import SSHClient, AutoAddPolicy
import yaml
import sys
import time
import pdb

def ssh_fgt(ipadd,portno,user,pwd,command,privatefile):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    try:
        if (privatefile==''):
            client.connect(ipadd,username=user,password=pwd,port=portno,timeout=10)
        else:
            client.connect(ipadd, username=user,port=portno, timeout=10, key_filename=privatefile)
    except:
        print("Can not connect to "+ipadd+':'+str(portno)+' with given credentials !!')
        exit()

    # try first using this and if it works just use this ? but remember the \r\n ?
#    stdin, stdout, stderr = client.exec_command(command)
#    hslexec = stdout.read()
    
#    if ( len(hslexec)>100 ):
#        print("Succesful using exec_command")
#        print(hslexec)
#        pdb.set_trace()
#        return hslexec


    # will need to find a more graceful way .. check the prompt ? now just sleep
    remote_shell = client.invoke_shell()
    print("Wait 2 seconds for ssh ready...")
    time.sleep(2)
    hasil=''
    while (len(hasil)<50):
        remote_shell.send(command+'\n')
        hasil = remote_shell.recv(500000)
        print('Wait 10 seconds for capturing long configuration.....')
        time.sleep(10)
        if (len(hasil)<50):
           print('Not getting enough data, got only '+str(len(hasil))+' bytes ....sleeping for 5 seconds..and will repeat ...')
           time.sleep(5) 
        else:
            print('Getting '+str(len(hasil))+' bytes')

    #print(hasil.decode())
    client.close()
    return hasil

def loadyaml2dict(namafile):
    try:
        f = open(namafile, "r")
    except:
        print(namafile+" can not be opened!")
        exit()

    sentdata = yaml.load(f, Loader=yaml.FullLoader)
    f.close()
    return sentdata

def find_config_module(modsearch,allconfig):
    awal = allconfig.find('config '+modsearch+'\r') # added \r to prevent real-server real-server-profile
    akhir = allconfig.find('\r\nend\r\n',awal+1)    
    return allconfig[awal:akhir+7]            # 7 = word '\r\nend\r\n'

def combine_module(conflengkap, listmodule):   # contoh listmodule = ['firewall policy','firewall ippool']
    allparts = ''
    for i in listmodule:
        findpart = find_config_module(i, conflengkap.decode())
        allparts = allparts + findpart + "\n" 
    return allparts

def savefile(teks,nmfile):
    f=open(nmfile,'w')
    f.write(teks)
    f.close()

def inject_script( scriptinject, listdeviceip ):  # listdeviceip = [ '1.1.1.1','2.2.2.2','3.3.3.3' ]
    for ip in listdeviceip:
        print ('Injecting script to '+ip)
     # not implemented yet !!!   

def main():
    try:
        namafile = sys.argv[1]
    except:
        print("Using default config get-config.yaml...  please supply filename is you want to use other configuration")
        namafile = 'get-config.yaml'
    
    isidata = loadyaml2dict(namafile)
    
    print("Please make sure that Forti product is config with config system console - set output standard, to prevent 'more' during ssh !!")
    print('Getting configuration....')
 
    try:
        useprivatekey = isidata['device']['privatekeyfile']
    except:
        useprivatekey = ''

    if (useprivatekey == ''):
        configstr = ssh_fgt(isidata['device']['ip'], isidata['device']['port'], 
                    isidata['device']['username'], isidata['device']['password'], isidata['device']['configcmd'] ,'' )
    else:
        configstr = ssh_fgt(isidata['device']['ip'], isidata['device']['port'], 
                    isidata['device']['username'], '', isidata['device']['configcmd'] , useprivatekey)

    f = open('cfgtmp.txt','w')
    f.write(configstr.decode())
    f.close()

    gabungmodule = combine_module( configstr, isidata['module'] )

    print(gabungmodule)

    savefile(gabungmodule,isidata['filename'])
    print('Combined module is saved successfully to '+isidata['filename'])

#    inject_script(gabungmodule, [ '1.1.1.1','2.2.2.2','3.3.3.3'])


if __name__ == "__main__":
    main()




'''
uji coba connect ke aws dg pem key
ada yg aneh dg kasus ssh ke aws, di mana pakai client.exec_command tidak dapat hasil apapun !
harus pakai invoke_shell
'''
