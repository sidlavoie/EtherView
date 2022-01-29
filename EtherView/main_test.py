import lib
interface = input("Entrez l'interface: ")

ip = lib.get_ip(interface)
netmask = lib.get_netmask(interface)
gateway = lib.get_default_gateway()
speed = lib.get_iface_speed(interface)
updown = lib.get_ifaceupdown(interface)


print("IP: %s, Netmask: %s, Gateway: %s, Speed: %s, Link: %s" % (ip,netmask,gateway,speed,updown))

result = lib.dhcp_reload(interface)

print(result)