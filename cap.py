#sudo chmod +x /usr/bin/dumpcap

import pyshark

cap=pyshark.LiveCapture(interface='eth0')
cap.sniff(timeout=10)

def print_info(packet):
  print("PROTOCOL:"+packet.highest_layer+"SOURCE IP:"+packet.ip.src+"DESTINATION:"+packet.ip.dst)
cap.apply_on_packets(print_info)
