# Copyright 2022 by Sidney Lavoie

# This is the main program for the EtherView project.
# It controls the display and fetches the functions from lib.py

import lib
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import strftime
import threading

root = Tk()  # Creates the main window
defbgn = "#EEf0F1"  # Default background color
timelbl = Label(root, background="#FFFFFF", relief="sunken", anchor="c", width=10)  # Label for time

class MainSettings:
    def __init__(self):
        self.dnshost = "google.com"
        self.iface = "bond0"  # Will be later eth0 when on the raspberrypi
        self.ping_num = 4

    def settings(self):  # Settings window
        settings_window = Toplevel(height=300, width=200)
        settings_window.title("Settings")

        def set_eth():
            wlan_button.config(state="normal")
            self.iface = "eth0"
            eth_button.config(state="disabled")

        def set_wlan():
            eth_button.config(state="normal")
            self.iface = "wlan0"
            wlan_button.config(state="disabled")
        # Buttons for setting interface
        eth_button = ttk.Button(settings_window, width=6, text="eth0", command=set_eth)
        wlan_button = ttk.Button(settings_window, width=6, text="wlan0", command=set_wlan)
        eth_button.place(x=10, y=10)
        wlan_button.place(x=73, y=10)

        # Changes the default host to check DNS
        def set_default_dnshost():
            self.dnshost = default_dns_input.get()
            default_dns_input.delete(0, "end")

        default_dns_button = ttk.Button(settings_window, width=14, text="Set DNS", command=set_default_dnshost)
        default_dns_input = ttk.Entry(settings_window)

        default_dns_button.place(x=10, y=70)
        default_dns_input.place(x=10, y=110, width=160, height=30)

        # Sets how many pings are performed
        def set_ping_num():
            self.ping_num = ping_num_entry.get()
            ping_num_entry.delete(0, "end")

        ping_num_button = Button(settings_window, width=14, text="Set ping number", command=set_ping_num)
        ping_num_entry = Entry(settings_window)

        ping_num_button.place(x=10, y=170)
        ping_num_entry.place(x=10, y=210, width=160, height=30)

    def get_ping_num(self):
        return self.ping_num

    def get_dnshost(self):
        return self.dnshost

    def get_iface(self):
        return self.iface


def time():  # Controls the clock
    string = strftime("%H:%M:%S %p")
    timelbl.config(text=string)
    timelbl.after(1000, time)


def do_ping():  # INCOMPLETE FOR NOW!!! Keypad is missing
    print("Opening Ping...")
    ping_window = Toplevel(height=350, width=800)
    ping_window.title("Ping")
    ping_window.focus_get()
    # for i in ["7", "8", "9", "4", "5", "6", "1", "2", "3", ".", "0", "Enter"]:
    ping_label = ttk.Label(ping_window, text="Enter host to ping", background=defbgn)
    ping_input = ttk.Entry(ping_window)
    ping_display = ttk.Label(ping_window, font="Courier 10", background="#000000",
                             foreground="#FFFFFF", padding=10, anchor="nw")

    def thread_ping():
        pb.start(15)
        threading.Thread(target=start_ping).start()
        return

    def start_ping():  # Calls the ping_test in lib
        host = str(ping_input.get())
        if host.isalpha() is False:
            do_ping_button.config(state="disabled")
            result = lib.ping_host(host, Main.get_ping_num())
            ping_display.config(text=result)
            do_ping_button.config(state="normal")
        else:
            messagebox.showwarning("Incorrect IP",  "Please enter a valid IPv4 address (xxx.xxx.xxx.xxx)")
        pb.stop()

    do_ping_button = ttk.Button(ping_window, command=thread_ping, text="Start")  # to Replace with keypad
    ping_display.place(x=10, y=10, width=590, height=330)
    ping_label.place(x=610, y=10, height=30)
    ping_input.place(x=610, y=45, width=160, height=30)
    do_ping_button.place(x=610, y=80)


def check_dns():  # Animates the button when press and displays info
    dns_button.config(state="disabled")
    response = lib.check_dns(Main.get_dnshost())

    while response is not True or not False:
        if response is True:
            messagebox.showinfo("Success", "DNS is connected\n%s is reachable"
                                % Main.dnshost)
            dns_button.config(state="normal")
            return True
        if response is False:
            messagebox.showwarning("Failed!", "DNS not connected!\nSpecified host unreachable")
            dns_button.config(state="normal")
            return False


def dhcp_reload():  # Sends command to release and reacquire DHCP
    messagebox.showinfo("Done", "Reload Complete!")
    lib.dhcp_reload(Main.get_iface())


def check_connexion():  # Runs every second to update the internet status.
    ip_address = "--"
    netmask = "--"
    default = "--"
    link = lib.get_ifaceupdown(Main.get_iface())
    link_speed = lib.get_iface_speed(Main.get_iface())
    if link == "Up":
        ip_address = lib.get_ip(Main.get_iface())
    if link == "Up":
        netmask = lib.get_netmask(Main.get_iface())
    if link == "Up":
        default = lib.get_default_gateway()

    out = "Interface: %s\n\nLink: %s\n\nLink speed: %s\n\n" \
          "IP Address: %s\n\nNetmask: %s\n\nDefault Gateway: %s" \
          % (Main.get_iface(), link, link_speed, ip_address, netmask, default)
    ip_info.config(text=out)
    if link == "Up":
        connect_lbl.config(text="Connected")
    else:
        connect_lbl.config(text="Not connected!")

    root.after(1000, check_connexion)


def test_speed_background():
    pb.start(15)
    messagebox.showinfo("Performing Speedtest...", "Operation may take a minute\nPress OK to continue")
    threading.Thread(target=test_speed).start()
    return


def test_speed():  # Does a Speedtest if the servers are reachable

    speed_button.config(state="disabled")

    result = lib.get_internet_speed()
    if result is False:
        messagebox.showwarning("Failed!", "Could not connect to Speedtest's severs. "
                                          "Please check your connexion and DNS")
        pb.stop()
    else:

        messagebox.showinfo("Speedtest", result)
    speed_button.config(state="normal")
    pb.stop()


def loading():
    pb.place(x=650, y=390)
    print("là")


def loading_destroy():
    print("ici")
    pb.place_forget()


Main = MainSettings()

root.title("EtherView Analyzer")
root.focus_force()
root.geometry("800x480")
# root.attributes("-fullscreen", True) # Uncomment to put fullscreen

ip_info = ttk.Label(root, font=10, padding=10, background="#FFFFFF", relief="sunken")
# Bottom of screen
time()
pb = ttk.Progressbar(root, orient="horizontal", mode="indeterminate")
pb.place(x=465, y=453, width=240)
timelbl.place(x=710, y=450)
connect_lbl = ttk.Label(root, background="#FFFFFF", relief="sunken", anchor="c")
connect_lbl.place(x=360, y=450, width=100, height=25)
# Other screen widgets
ping_button = Button(root, text="Ping", command=do_ping, background="firebrick2")
dns_button = Button(root, text="DNS test", command=check_dns, background="green3")
dhcp_button = Button(root, text="Reload DHCP", command=dhcp_reload, background="DeepSkyBlue2")
speed_button = Button(root, text="Speed test", command=test_speed_background, background="darkorange2")
settings_button = Button(root, text="Settings", command=Main.settings, background="gold")
static_button = Button(root, text="Static IP", command="none", background="darkorchid2")

first_column = 470
second_column = 630

ip_info.place(x=10, y=10, width=440, height=320)
ping_button.place(x=first_column, y=10, width=150, height=100)
dns_button.place(x=second_column, y=10, width=150, height=100)
dhcp_button.place(x=first_column, y=120, width=150, height=100)
speed_button.place(x=second_column, y=120, width=150, height=100)
settings_button.place(x=first_column, y=230, width=150, height=100)
static_button.place(x=second_column, y=230, width=150, height=100)

check_connexion()
root.mainloop()
