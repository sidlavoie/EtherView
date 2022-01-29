import socket
import netifaces
import struct
import subprocess
import speedtest


def get_ip(iface):  # Gets the Raspi's IPv4 address
    try:
        address = netifaces.ifaddresses(iface)
        ip_addr = address[netifaces.AF_INET][0]['addr']

        return ip_addr

    except KeyError:
        return "N/A"


def get_netmask(iface):  # Gets the Raspi's netmask in the 255.255.255.0 format
    try:
        address = netifaces.ifaddresses(iface)
        netmask = address[netifaces.AF_INET][0]['netmask']

        return netmask

    except KeyError:
        return "N/A"


def get_default_gateway():  # Gets the Raspi's default gateway
    with open("/proc/net/route") as fh:
        for line in fh:
            fields = line.strip().split()
            if fields[1] != "00000000" or not int(fields[3], 16) & 2:
                continue

            return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))


def get_iface_speed(iface):  # Gets the reported speed of the interface the Raspi is connected to.
    try:
        speed = subprocess.getstatusoutput("ethtool " + iface + " | grep Speed")
        speed = str(speed[1])
        speed = speed.split(" ")
        return speed[5]

    except IndexError:
        return "N/A"


def get_ifaceupdown(iface):  # Gets the status of the internet interface
    i = subprocess.getstatusoutput("cat /sys/class/net/" + iface + "/operstate")
    i = i[1]
    if i != "down":
        return "Up"
    else:
        return "Down"


def ping_host(host, number):  # Host should be an IP address. Pings a host a number of time and gets the output
    number = str(number)
    print("Starting ping. This may take a minute...")
    ping = subprocess.getstatusoutput("ping -c " + number + " " + host)
    print("Ping done")

    return ping[1]


def check_dns(host):  # Host should be a domain name. Returns true if the Raspi can access that domain
    print("Checking DNS. May take a minute...")
    result = subprocess.getstatusoutput("ping -c 1 " + host)
    if result[0] == 0:
        return True

    else:
        return False


def get_internet_speed():  # Checks connectivity to speedtest.net. Then output the upload and download speed in a string
    result = subprocess.getstatusoutput("ping -c 2 speedtest.net")
    if result[0] != 0:
        print("Could not connect. Retrying...")
        result = subprocess.getstatusoutput("ping -c 2 speedtest.net")
        if result[0] != 0:
            return False

    print("Performing speedtest...")
    inter = speedtest.Speedtest()
    down = inter.download()
    up = inter.upload()
    down = round(down / 1000000, 2)
    up = round(up / 1000000, 2)

    return ("Download: %s Mb/s, Upload: %s Mb/s" %(down, up))


def dhcp_reload(iface):  # Requests a new DHCP lease
    rel = subprocess.getstatusoutput("dhclient -r %s && sudo dhclient %s" %(iface, iface))
    print("Reloading dhcp...")

    return rel[1]




