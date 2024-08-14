from scapy.all import *


def packet_callback(packet):
    print(packet.show())


# Sniff packets on the Wi-Fi interface
sniff(iface='Wi-Fi', prn=packet_callback, count=10)
