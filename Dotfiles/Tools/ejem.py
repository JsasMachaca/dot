import scapy.all as scapy

a = {"ip":12345, "mac":54321}
l = []

l.append(a)
print(a["ip"])
print(l)
for i in l:
    print(i)