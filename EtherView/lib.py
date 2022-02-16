# Copyright 2022 by Sidney Lavoie

# This document holds the functions for the EtherView Project

import socket
import netifaces
import struct
import subprocess
import speedtest
import urllib.request
import os


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
        return speed[1]

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
    ping = subprocess.getstatusoutput("ping -c " + number + " " + host)

    return ping[1]


def check_dns(host):  # Host should be a domain name. Returns true if the Raspi can access that domain
    result = subprocess.getstatusoutput("ping -c 1 " + host)
    if result[0] == 0:
        return True

    else:
        return False


def get_internet_speed():  # Checks connectivity to speedtest.net. Then output the upload and download speed in a string
    result = subprocess.getstatusoutput("ping -c 2 speedtest.net")
    if result[0] != 0:
        # print("Could not connect. Retrying...")
        result = subprocess.getstatusoutput("ping -c 2 speedtest.net")
        if result[0] != 0:
            return False

    # print("Performing speedtest...")
    inter = speedtest.Speedtest()
    down = inter.download()
    up = inter.upload()
    down = round(down / 1000000, 2)
    up = round(up / 1000000, 2)
    # print("Speedtest done!")

    return ("Download: %s Mb/s\nUpload: %s Mb/s" % (down, up))


def dhcp_reload(iface):  # Requests a new DHCP lease
    rel = subprocess.getstatusoutput("sudo systemctl restart dhcpcd" % (iface, iface))
    # print("Reloading dhcp...")

    return rel[1]


def get_arp_neighbors():
    arp = subprocess.getstatusoutput("arp -ev")
    return arp[1]


def get_public_ip():
    public = urllib.request.urlopen("https://ident.me").read().decode("utf8")
    return public


def iperf_client(host):
    response = subprocess.getstatusoutput("iperf3 -c " + host)
    return response


def change_ip(interface, ip, mask, gateway, dns):
    subprocess.getstatusoutput("sudo cp /etc/dhcpd.conf /etc/dhcpd.conf.old")
    oldfile = open("/etc/dhcpcd.conf", "r")
    data = str(oldfile.readline())
    oldfile.close()
    change = str("\ninterface " + interface + "\nstatic ip_address=" + ip + mask +
                 "\nstatic routers=" + gateway + "\nstatic domain_name_servers=" + dns)
    file = open("dhcpcd.conf", "a")
    file.truncate(0)
    file.write(data)
    file.write(change)
    file.close()
    os.system("sudo mv dhcpcd.conf /etc")
    os.system("sudo systemctl restart dhcpcd")


def restore_dhcp():
    subprocess.getstatusoutput("sudo mv /etc/dhcpcd.conf.old /etc/dhcpcd.conf && sudo systemctl restart dhcpcd")
