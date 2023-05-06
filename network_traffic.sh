timestamp=$(date +%d.%m.%Y-%H.%M)
mkdir -p network_traffic_logs && cd network_traffic_logs
touch $timestamp.pcap && sudo tshark -i eth0 -a filesize:100000 -w $timestamp.pcap --color
