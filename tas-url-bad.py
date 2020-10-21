# tas-url-bad.py norequest yes|no
# 
# eg tas-url-bad.py 10 yes
#
#            will run 10 first line ( default = all )
#            yes - redownload from urlhaus.abuse.ch ( default = use the existing file url-list.csv )
#

import requests
import sys
import pdb
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def downloadfile(namafile):
    r = requests.get('https://urlhaus.abuse.ch/downloads/csv_online/', timeout=10, verify=False)
    f = open(namafile,"w")
    f.write(r.text)
    f.close()

def akses(baris):
    try:
        r = requests.get(baris, verify=False, timeout=1 )
        return int(r.headers['Content-Length'])
    except:
        return -1

def main():
    try:
        jumlah = int(sys.argv[1])
    except:
        jumlah = 0
    
    try:
        if (sys.argv[2]=='yes'):
            redo = True
        else:
            redo = False
    except:
            redo = False
    
    if (redo):  # just redownload only if needed
       downloadfile('url-list.csv')
    
    f = open('url-list.csv')
    i = 0
    for line in f:
        data = line.split(",")
        
        i = i + 1
        if ( jumlah!=0 ):
            if ( jumlah == i+1 ):
                print("Stopped")
                exit()

        try:
            url = data[2]
            result = akses(url.replace('"',''))
            if ( result > 1):
                print ("OK - Size:"+ str(result)+" "+url)
            else:
                print ("** NOT OK -"+url)

        except IndexError as error: # url not found so ignore this
            print("IGNORED - "+line)
            pass

    f.close()

if (__name__=='__main__'):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    main()
