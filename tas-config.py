from paramiko import SSHClient, AutoAddPolicy
import sys
import pdb

def ssh_fgt(ipadd,portno,user,pwd,command):
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    client.connect(ipadd,username=user,password=pwd,port=portno)
    print ("Executing :"+command)
    stdin, stdout, stderr = client.exec_command(command)
    hasil = stdout.read()
    client.close()
    return hasil

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

def inject_script( scriptinject, listdeviceip ):  # listdeviceip = [ '1.1.1.1','2.2.2.2','3.3.3.3' ]
    for ip in listdeviceip:
        print ('Injecting script to '+ip)
     # not implemented yet !!!   

def main():
    print("Please make sure that fortigate is config with config system console - set output standard")
    print('Getting configuration....')
    configstr = ssh_fgt('192.168.1.99', 22, 'testing', '12345', 'show' )

    gabungmodule = combine_module( configstr, [ 'system interface','firewall policy','firewall ippool', 'router ospf' ] )

    print(gabungmodule)

    inject_script(gabungmodule, [ '1.1.1.1','2.2.2.2','3.3.3.3'])


if __name__ == "__main__":
    main()


'''

pola config yg sulit yg spt :

config router rip
    config redistribute "connected"
    end
    config redistribute "static"
    end
    config redistribute "ospf"
    end
    config redistribute "bgp"
    end
    config redistribute "isis"
    end
end

yg bagian ini nanti dulu

#    print('Full configuration :')
#    print('-----------------------')
#    print(configstr.decode())  # use decode to translate b' and \n

#    ada = find_config_module('kagak ada',configstr.decode())
#    if not ada:
#        print('contoh bagian tidak ketemu')

find config, ketemu posisi 1

cari lagi 'config' mulai dari posisi 1 -> posisi nextconfig
cari juga 'end' mulai dari posisi 1  -> posisi nextend
if nextconfig < nextend --> ini berarti nested

'''
