import scapy.all as scapy


def scan(ip):
    arp_request = scapy.ARP(pdst=ip) #creación de un paquete ARP para obtener ip
    broad = scapy.Ether(dst='ff:ff:ff:ff:ff:ff') #creación de un broadcast
    arp_broad = broad/arp_request #creacion de un objeto arp que será enviado por broadcast
    answered  = scapy.srp(arp_broad, timeout=1, verbose=False)[0] #obtención de una respuesta al enviar el paquete arp broadcast

    client = [] #lista que contendrá un iterable con las respuestas del broadcast 
    for element in answered:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc, "me": element[1].pdst} #diccionario que contiene las respuestas del broadcast (ip, mac, y mi ip)
        client.append(client_dict)

    return client

 # funcion que imprime una cabazera del programa
def results(results_list):
    print('IP\t\t\tMAC address\t\t\tDestination(Me)')
    print(70 * "-")
    for clients in results_list:
        print(clients["ip"] + "\t\t" + clients["mac"] + "\t\t" + clients["me"])


gat = "192.168.1.1/24"
results(scan(gat))
