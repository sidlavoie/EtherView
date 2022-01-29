# EtherView
Last updated jan 29, 2022.

## Welcome to EtherView!

This is a work in progress to transform a RaspberryPi into a portable network diagnostic machine.

The goal of this project is to make a custom Linux distro to enable basic network diagnostic using a RaspberryPi with a touchscreen.
I do not know how long I will maintain this project or how many bugs I will fix. I just want it to run.

The upcoming Linux distro will be based on RaspberryPi OS Lite and will launch a custom python application 
which will enable connectivity tests without the use of a keyboard.

### Hardware
The hardware will be a RaspberryPi 3 or 4, with the official touchscreen. A cse will also be used to improve ruggedness, but is optional.
The main goal would be to run the Pi and screen on a battery, be it a USB power bank, or an integrated lithium battery and charger.

### Currently done
- Obtain status of network interface(up/down)
- Obtain basic network information (IPv4 address, netmask, default gateway) on a DHCP enabled network.
- Ping a host using IPv4 address.
- Check DNS connectivity
- Test link speed of network interface and internet speed
- Reload DHCP configuration
- Basic GUI which shows connectivity
- App can be forced to fullscreen

### To be done
- Enable the user to set a static IP address
- Complete the GUI, make it prettier
- Create a settings menu
- Create a disk image of a minimal RaspberryPi OS-based distro which runs the python app in a kiosk mode (only app at boot)

### Nice to have (maybe will be done, but are not the current focus)
- Clock
- Find a way to redirect the console output to the GUI (some functions have helper prints)
- Enable the user to connect to wlan
- Log data using PyShark
- See visible hosts on network
- SSH shell (will need either a virtual or physical keyboard)
- Reference charts (maybe you network engineers can tell me which references you would like to have)
- See the DNS server
- Network performance graph (speed, latency...)

### Can you do that? (nice ideas that may require extensive modifications of the OS or may not be possible)
- Log network traffic
- View VLANS
- View and connect to domains
- View control packets
- Check cable length
- Check cable wiring (maybe using a USB ethernet dongle or the GPIO pins)
- Serial port
- Remote wifi connection to a cellphone to enable wireless control.
- TeamViewer integration?

### Known limitations
- Since the interface on the Raspberry is only gigabit, it may not be possible to test faster networks. 
  It wil work but the speed most likely will show 1 Gb/s (but hey, it's a 180$ network analyser, what did you expect).
- Since it is using terminal commands and lookup of specific files, it will most likely break one day when a update is performed to RaspberryPi OS. 
  But most likely not next week.
- There WILL be some security flaws. It is not intended to be a highly secure device, only a small tool for network enthusiasts. Use it at your own risk.
- May not work on future Pi models.
  
  
If you support the project or have any questions, feel free to send me an email at lavoiesidney@gmail.com
