timestamp=$(date +%d.%m.%Y-%H.%M)
mkdir -p arp_traffic_logs && cd arp_traffic_logs
#touch $timestamp && sudo tshark -i eth0 -a filesize:100000 -w $timestamp --color --enable-protocol ARP 
touch $timestamp.pcap && sudo tcpdump -i eth0 arp -v -w $timestamp.pcap 