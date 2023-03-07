import nmap 

scan = nmap.PortScanner()
ip = "192.168.1.1/24"

scan(ip)
print(scan.all_hosts())

    