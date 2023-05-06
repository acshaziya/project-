

# Address Resolution Protocol Spoofing

## Problem Statement
Most of the organizations implement LAN for their communication and networking needs. In LANs, the identifier used for communication is MAC address. Thus, transfer of packets require resolving IP address to MAC address for communication within a LAN. This resolution is done by the Address Resolution Protocol (ARP).
However, this protocol suffers a major security issue. ARP protocol is stateless. It does not authenticate whether any request was made for the response received. Thus, it becomes prone to an attack known as ARP spoofing attack.

## Objective of the Project
The main objective the project is to address two issues; first, is to identify the attacker and second, is to prevent the ARP Spoofing attack. 
The attacker will spoof the MAC address to perform ARP spoofing. The goal here would be to check for spoofed MAC address and to prevent the attack by notifying the administrator via email.


## Installation and Usage

1. Clone the repository.
2. Requirements: Kali Linux , Python
3. Install the requirement file
4. Use the following commands:
- cd ARP Spoof Detector
- sudo nano email_alerts.py  
    - Edit the following details
```Edit the following details
  username = 'Enter your email id'
  password = 'Enter your password token'
  sender = 'Enter your name'
  targets = ['Enter an email address']
``` 
- sudo chmod 777 arp_traffic.sh network_traffic.sh main.sh
- ./main.sh 


   

