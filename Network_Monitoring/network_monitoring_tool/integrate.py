import os  # noqa
import django  # noqa
from scapy.all import sniff, IP
import nmap

# Set up Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'network_monitoring_tool.settings')  # noqa
django.setup()  # noqa

from monitor.models import Vulnerability


def packet_callback(packet):
    ip_layer = packet.getlayer(IP)
    if ip_layer:
        print(f'IP Packet: {ip_layer.src} -> {ip_layer.dst}')
        nmap_scan(ip_layer.src)


def nmap_scan(target):
    nm = nmap.PortScanner()
    nm.scan(target, '1-1024', '-sV')
    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                new_vuln = Vulnerability(
                    host=host,
                    port=port,
                    service=nm[host][proto][port]['name'],
                    state=nm[host][proto][port]['state']
                )
                new_vuln.save()


if __name__ == '__main__':
    sniff(iface='Wi-Fi', prn=packet_callback, count=10)
