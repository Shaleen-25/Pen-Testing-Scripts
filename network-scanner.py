

#Pyhton Script to scan all devices on the same network as yours
#Type [python network-scanner.py] to get a list of all IP and MAC address on your network
#!usr/bin/env pyhton


import scapy.all as scapy
import re

def scan(ip):
    arp_req=scapy.ARP(pdst=ip)
    # arp_req.show()
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # broadcast.show()
    arp_req_broadcast=broadcast/arp_req
    # arp_req_broadcast.show()
    # print(arp_req_broadcast.summary())
    yes = scapy.srp(arp_req_broadcast, timeout =1, verbose=False)[0]
    # no = scapy.srp(arp_req_broadcast, timeout =1)[1]
    print("\nIP\t\t\tMAC\n-----------------------------------------------")
    for i in yes :
        print(i[1].psrc+ "\t\t"+ i[1].hwsrc)
        #i[0] has the list of sent packets, while i[1] has the list of recieved packets
        print("-----------------------------------------------")

opt=input("\nEnter 1 to enter single IP address(without subnet mask) or \nEnter 2 IP range (with subnet mask) to start the scan \nEnter your option -> ")

if opt==1:
    ip_add=raw_input("Enter IP [eg: 10.55.12.41] -> ")
    bool= re.match(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",ip_add)
    if not bool:
        print("[-]Enter Relevant IP Address ")
    else:
        scan(ip_add)
else:
    ip_add = raw_input("Enter IP range[eg: 10.55.12.41/24] -> ")
    bool = re.match(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/*/\d{1,2}\b", ip_add)
    if not bool:
        print("[-]Enter Relevant IP Address Range")
    else:
         scan(ip_add)
