import socket
import netifaces
import struct
import subprocess
import speedtest

def get_ip(iface):
    try:
        address = netifaces.ifaddresses(iface)
        ip_addr = address[netifaces.AF_INET][0]['addr']

        return ip_addr

    except KeyError:
        return "N/A"


def get_netmask(iface):
    try:
        address = netifaces.ifaddresses(iface)
        netmask = address[netifaces.AF_INET][0]['netmask']

        return netmask

    except KeyError:
        return "N/A"


def get_default_gateway():
    with open("/proc/net/route") as fh:
        for line in fh:
            fields = line.strip().split()
            if fields[1] != "00000000" or not int(fields[3], 16) & 2:
                continue

            return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))


def get_iface_speed(iface):
    try:
        speed = subprocess.getstatusoutput("ethtool " + iface + " | grep Speed")
        speed = str(speed[1])
        speed = speed.split(" ")
        return speed[5]

    except IndexError:
        return "N/A"


def get_ifaceupdown(iface):
    i = subprocess.getstatusoutput("cat /sys/class/net/" + iface + "/operstate")
    i = i[1]
    if i != "down":
        return "Up"
    else:
        return "Down"


def ping_host(host, number):
    number = str(number)
    print("Starting ping. This may take a minute...")
    ping = subprocess.getstatusoutput("ping -c " + number + " " + host)

    return ping[1]


def check_dns(host):
    print("Checking DNS. May take a minute...")
    result = subprocess.getstatusoutput("ping -c 1 " + host)
    if result[0] == 0:
        return True

    else:
        return False


def check_speed

interface = input("Entrez l'interface")

ip = get_ip(interface)
netmask = get_netmask(interface)
gateway = get_default_gateway()
speed = get_iface_speed(interface)
updown = get_ifaceupdown(interface)


print("IP: %s, Netmask: %s, Gateway: %s, Speed: %s, Link: %s" % (ip,netmask,gateway,speed,updown))
ping = ping_host("192.168.0.2", "10")
print(ping)

