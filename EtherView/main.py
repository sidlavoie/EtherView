import lib
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox

defbgn = "#EEf0F1" # Default background color
dnshost = "google.com"
iface = "bond0"  # Will be later eth0 when on the raspberrypi


def do_ping():  # INCOMPLETE FOR NOW!!!
    print("Opening Ping...")
    ping_window = Toplevel(height=400, width=400)
    ping_window.focus_get()
    # for i in ["7", "8", "9", "4", "5", "6", "1", "2", "3", ".", "0", "Enter"]:
    ping_label = ttk.Label(ping_window, text="Enter host to ping",background=defbgn)
    ping_input = ttk.Entry(ping_window)
    ping_label.place(x=210, y=10, height=30)
    ping_input.place(x=210, y=45, width=160, height=30)


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


root = Tk()
root.title("EtherView Analyzer")
root.focus_force()
root.geometry("800x480")
# root.attributes("-fullscreen", True) # Uncomment to put fullscreen

ip_info = ttk.Label(root, font=("FreeSans", 20), padding=10)

ping_button = Button(root, text="Ping", command=do_ping, background="orange red")
dns_button = Button(root, text="DNS Test", command=check_dns, background="lime green")
dhcp_button = Button(root, text="Reload DHCP", command=dhcp_reload, background="deep sky blue")

ip_info.place(x=10, y=10, width=380, height=380)
ping_button.place(x=470, y=10, width=150, height=150)
dns_button.place(x=630, y=10, width=150, height=150)
dhcp_button.place(x=470, y=170, width=150, height=150)

check_connexion()
root.mainloop()
