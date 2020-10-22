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
import argparse

def downloadfile(namafile,proxyaddress):
    print("Redownloading url malware list from urlhaus.abuse.ch ....")
    r = requests.get('https://urlhaus.abuse.ch/downloads/csv_online/', proxies = proxyaddress)
    f = open(namafile,"w")
    f.write(r.text)
    f.close()
    print("URL Malware List downloaded")

def akses(baris,proxyaddress):
    try:
        r = requests.get(baris, verify=False, timeout=1, proxies = proxyaddress )
        return int(r.headers['Content-Length'])
    except:
        return -1

def main():
    print("tas-url-bad.py v0.1 by TAS ATX")
    print("-------------------------------")
    parser=argparse.ArgumentParser(description="tas-url-bad.py will require some argument to run")
    parser.add_argument("limit", help='Run until line number limit',type=int)
    parser.add_argument("--download", help="Redownload the list from abuse.ch or not", action='store_true')
    parser.add_argument("--useproxy", help="Run with Proxy Server, specify your proxy server user:pass@1.1.1.1:9999")
    args = parser.parse_args()

    jumlah = args.limit
    redo = args.download
    useproxy = args.useproxy

    if ( useproxy!=None ):
        proxydict = { 'http':'http://'+useproxy, 'https':'http://'+useproxy}
    else:
        proxydict = {}

    if (redo):  # just redownload only if needed
       downloadfile('url-list.csv', proxydict)
    
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
            result = akses(url.replace('"',''), proxydict)
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
