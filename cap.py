#sudo chmod +x /usr/bin/dumpcap

import pyshark
cap=pyshark.LiveCapture(interface='eth0')
cap.sniff(timeout=10)
