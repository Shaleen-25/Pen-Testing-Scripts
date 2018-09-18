

# Python3 script to easily change MAC Address of desired Interfaces before indulging in any Pen-Testing activities.
# Type [ pyhton mac-changer.py ] on terminal to execute the script

import subprocess
import re

interface=input("Enter Interface(eg: eth0,wlan0) -> ")
new_mac=input("Enter New_MAC(eg> 00:11:22:33:44:55 ) -> ")
chk=re.match(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",new_mac)
if not chk:
     print("[-] Enter Relevant MAC Address ")

def getmac(interface):
    try:
        mac = open('/sys/class/net/'+interface+'/address').readline()
    except:
        mac = "00:00:00:00:00:00"

    return mac[0:17]

old_mac = getmac(interface)

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
subprocess.call(["ifconfig",interface,"up"])
final_mac=getmac(interface)
if(final_mac==new_mac):
     print("[+] MAC address for "+interface+" has been successfully changed from "+ old_mac+ " to "+new_mac +" \n")
else:
    print ("[-] Could not change MAC Address")



