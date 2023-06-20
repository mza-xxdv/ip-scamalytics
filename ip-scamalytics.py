
import requests
from bs4 import BeautifulSoup
import sys
import os
from datetime import datetime

print(f'mohon tunggu . . . .')

def validIPAddress(IP):
    """
    :type IP: str
    :rtype: str
    """

    def isIPv4(s):
        try:
            return str(int(s)) == s and 0 <= int(s) <= 255
        except:
            return False

    def isIPv6(s):
        if len(s) > 4:
            return False
        try:
            return int(s, 16) >= 0 and s[0] != '-'
        except:
            return False

    if IP.count(".") == 3 and all(isIPv4(i) for i in IP.split(".")):
        return "IPv4"
    if IP.count(":") == 7 and all(isIPv6(i) for i in IP.split(":")):
        return "IPv6"
    return "Neither"

versionfo = r'''
    ______                     __   ________ 
   / ____/________ ___  ______/ /  /  _/ __ \
  / /_  / ___/ __ `/ / / / __  /   / // /_/ /
 / __/ / /  / /_/ / /_/ / /_/ /  _/ // ____/ 
/_/   /_/   \__,_/\__,_/\__,_/  /___/_/     
                                             
         by @E_9mm -- v0.01
'''

reqview  = requests.get('http://ip-api.com/json/').json()
ipsaya = reqview['query']
isp = reqview['as']
country = reqview['country']
region_name = reqview['regionName']
city = reqview['city']
timezone = reqview['timezone']

endpoint = f"https://scamalytics.com/ip/{ipsaya}"
IPresult = validIPAddress(f"{ipsaya}")

try:
    r = requests.get(endpoint)
    htmlresponse = r.text
    soup = BeautifulSoup(htmlresponse, 'html.parser')
    coderet = soup.find_all(class_="panel_title high_risk")
    finalstuff = str(coderet)
    amb = str(finalstuff.split("\">")[1].split("</")[0])
    coderet = str(soup.find_all(class_="panel_body"))
    coderet1 = str(soup.find_all(class_="score"))

    print('=====================================')
    print('        Informasi Ip Address         ')
    print('=====================================')
    print('IP\t : ' + ipsaya)
    print('ISP\t : ' + isp)
    print('City\t : ' + city)
    print('Region\t : ' + region_name)
    print('Country\t : ' + country)
    print('Timezone : ' + timezone)
    print('=====================================')
    print('FraudInfo')
    print(amb + ' ; ' + coderet1.replace('[<div class="score">','').replace('</div>]','/100'))
    print("")
    print('Jika tidak yakin, silahkan cek manual')
    print(f'https://scamalytics.com/ip/{ipsaya}')
    print(os.linesep)
    print('====Response Info')
    print(coderet.replace('[<div class="panel_body">','').replace('<b>','').replace('</b>','').replace('Scamalytics','We').replace('</div>]','').replace('  ',' '))
    print('====END')

except:
    try:
        if (finalstuff.find("private IP address.")):
            print("The IP Address you provided is local and not a public one. Please refer to https://www.h3xed.com/web-and-internet/whats-the-difference-between-external-and-local-ip-addresses for more info")
        else:
            print("Connection Error, This program needs internet to function.")
    except:
        print("Unknown Error Occurred, Possibly Network Restrictions.")

sys.exit()
