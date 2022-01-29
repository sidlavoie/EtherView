import lib
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


defbgn = "#EEf0F1" # Default background color
dnshost = "google.com"
global iface
iface = "bond0"  # Will be later eth0 when on the raspberrypi
ping_num = 4


def do_ping():  # INCOMPLETE FOR NOW!!!
    print("Opening Ping...")
    ping_window = Toplevel(height=350, width=800)
    ping_window.title("Ping")
    ping_window.focus_get()
    # for i in ["7", "8", "9", "4", "5", "6", "1", "2", "3", ".", "0", "Enter"]:
    ping_label = ttk.Label(ping_window, text="Enter host to ping",background=defbgn)
    ping_input = ttk.Entry(ping_window)
    ping_display = ttk.Label(ping_window, font="Courier 10", background="#000000", foreground="#FFFFFF", padding=10, anchor="nw")

    def start_ping():
        host = str(ping_input.get())
        if host.isalpha() is False:
            do_ping_button.config(state="disabled")
            result = lib.ping_host(host, ping_num)
            ping_display.config(text=result)
            do_ping_button.config(state="normal")
        else:
            messagebox.showwarning("Incorrect IP",  "Please enter a valid IPv4 address (xxx.xxx.xxx.xxx)")

    do_ping_button = ttk.Button(ping_window, command=start_ping, text="Start") # to Replace with keypad
    ping_display.place(x=10, y=10, width=590, height=330)
    ping_label.place(x=610, y=10, height=30)
    ping_input.place(x=610, y=45, width=160, height=30)
    do_ping_button.place(x=610, y=80)


def check_dns():  # Animates the button when press and displays info
    dns_button.config(state="disabled")
    response = lib.check_dns(dnshost)

    while response is not True or not False:
        if response is True:
            messagebox.showinfo("Success", "DNS is connected")
            dns_button.config(state="normal")
            return True
        if response is False:
            messagebox.showwarning("Failure", "DNS does not appear to be connected!")
            dns_button.config(state="normal")
            return False
        #else:
            #print("Waiting for test...")


def dhcp_reload():
    messagebox.showinfo("Done", "Reload Complete!")
    lib.dhcp_reload(iface)


def check_connexion():
    ip_address = "--"
    netmask = "--"
    default = "--"
    link = lib.get_ifaceupdown(iface)
    if link == "Up":
        ip_address = lib.get_ip(iface)
    if link == "Up":
        netmask = lib.get_netmask(iface)
    if link == "Up":
        default = lib.get_default_gateway()

    out = "Interface: %s\n\nLink: %s\n\nIP Address: %s\n\nNetmask: %s\n\nDefault Gateway: %s" %(iface, link, ip_address, netmask, default)
    ip_info.config(text=out, anchor="nw")
    root.after(1000, check_connexion)


def settings():
    settings_window = Toplevel(height=350, width=800)
    settings_window.title("Settings")

    def set_eth():
        wlan_button.config(state="normal")
        iface = "eth0"
        eth_button.config(state="disabled")

    def set_wlan():
        eth_button.config(state="normal")
        iface = "wlan0"
        wlan_button.config(state="disabled")
    eth_button = ttk.Button(settings_window, width=6, text="eth0", command=set_eth)
    wlan_button = ttk.Button(settings_window, width=6, text="wlan0", command=set_wlan)
    eth_button.place(x=340, y=10)
    wlan_button.place(x=410, y=10)


root = Tk()
root.title("EtherView Analyzer")
root.focus_force()
root.geometry("800x480")
# root.attributes("-fullscreen", True) # Uncomment to put fullscreen

ip_info = ttk.Label(root, font=("Courier 10", 20), padding=10, background=defbgn, relief="sunken")

ping_button = Button(root, text="Ping", command=do_ping, background="orange red")
dns_button = Button(root, text="DNS Test", command=check_dns, background="lime green")
dhcp_button = Button(root, text="Reload DHCP", command=dhcp_reload, background="deep sky blue")
settings_button = Button(root, text="Settings", command=settings, background="yellow")

first_column = 470
second_column = 630

ip_info.place(x=10, y=10, width=380, height=380)
ping_button.place(x=first_column, y=10, width=150, height=100)
dns_button.place(x=second_column, y=10, width=150, height=100)
dhcp_button.place(x=first_column, y=120, width=150, height=100)
settings_button.place (x=first_column, y=230, width=150, height=100)

check_connexion()
root.mainloop()
