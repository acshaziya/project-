import scapy.all as scapy
import netifaces
import os, subprocess
from colorama import init, Fore, Back, Style
from datetime import datetime
import time


if os.getuid() != 0:
	print(Style.BRIGHT + Fore.RED)
	print ("This script require root privileges.")

else:
### ARP SPOOF DETECTOR & ALERT ADMINISTRATOR
	def get_mac(ip):
		arp_request=scapy.ARP(pdst=ip)
		broadcast_mac=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
		arp_broadcast = broadcast_mac/arp_request
		answered_l=scapy.srp(arp_broadcast, timeout=1, verbose=False)[0]
		return answered_l[0][1].hwsrc

	def sniff(interface):
		scapy.sniff(iface=interface,store=False,prn=sniffed_packet)

	def sniffed_packet(packet):
		if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
			try:
				real_mac = get_mac(packet[scapy.ARP].psrc)
				response_mac = packet[scapy.ARP].hwsrc 
				if real_mac != response_mac:
					print(Style.BRIGHT + Fore.RED)
					date = datetime.now().strftime("%I:%M:%S_%p")
					print (date+" -> You are under attack @ "+response_mac+"!!")
					os.system("sudo python email_alerts.py") & time.sleep( 120 )
			except:
				pass
	print("\nHere's a list of interfaces in your system: ")
	inter=(netifaces.interfaces())
	for i in inter:
		print(Style.BRIGHT + Fore.YELLOW)
		(print("\t"+i))
	#print("\n")
	print(Style.BRIGHT + Fore.WHITE)
	interface=input("Choose the desired interface: ")
	sniff(interface)
	print("\n")
