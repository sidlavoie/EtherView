import netifaces

print(netifaces.interfaces())

addrs = netifaces.ifaddresses('enp6s0')

ip_addr = addrs[netifaces.AF_INET][0]['addr']
netmask = addrs[netifaces.AF_INET][0]['netmask']
print(netmask)
print(ip_addr)