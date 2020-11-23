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

'''
from paramiko import SSHClient, AutoAddPolicy
import yaml
import sys

def ssh_fgt(ipadd,portno,user,pwd,command):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    try:
        client.connect(ipadd,username=user,password=pwd,port=portno,timeout=10)
    except:
        print("Can not connect to "+ipadd+':'+str(portno)+' with given credentials !!')
        exit()
    
    stdin, stdout, stderr = client.exec_command(command)
    hasil = stdout.read()
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
    awal = allconfig.find('config '+modsearch)
    akhir = allconfig.find('\nend\n',awal+1)    # make sure end\n --> if without \n can be 'set endip' considered as found!!! also belakangan found \nend bisa utk end of module utk config bernested
    return allconfig[awal:akhir+5]            # 3 = word 'end'

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
    
    configstr = ssh_fgt(isidata['device'][0]['ip'], isidata['device'][1]['port'], 
                isidata['device'][2]['username'], isidata['device'][3]['password'], isidata['device'][4]['configcmd'] )

    gabungmodule = combine_module( configstr, isidata['module'] )

    #print(gabungmodule)

    savefile(gabungmodule,isidata['filename'])
    print('Combined module is saved successfully to '+isidata['filename'])

#    inject_script(gabungmodule, [ '1.1.1.1','2.2.2.2','3.3.3.3'])


if __name__ == "__main__":
    main()
