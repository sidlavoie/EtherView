# EtherView
Last updated jan 30, 2022.

## Welcome to the EtherView project!

This is a project to transform a RaspberryPi into a portable network diagnostic machine.

The goal of this project is to make a custom Linux distro to enable basic network diagnostic using a RaspberryPi with a touchscreen.
I do not know how long I will maintain this project or how many bugs I will fix. I just want it to run.

The upcoming Linux distro will be based on RaspberryPi OS Lite and will launch a custom python application 
which will enable connectivity tests without the use of a keyboard.

### Hardware
The hardware will be a RaspberryPi 3 or 4, with the official touchscreen. A case will also be used to improve ruggedness, but is optional.
The main goal would be to run the Pi and screen on a battery, be it a USB power bank or an integrated lithium battery and charger.

### Currently done
- Obtain status of network interface(up/down)
- Obtain basic network information (IPv4 address, netmask, default gateway) on a DHCP enabled network.
- Ping a host using IPv4 address.
- Check DNS connectivity
- Test link speed of network interface and internet speed
- Reload DHCP configuration
- Basic GUI which shows connectivity
- App can be forced to fullscreen
- Pop-ups alert the user if something is wrong
- Working progress bar for long requests
- Clock
- Basic settings menu (for interface, number of ping and host to check DNS)

### To be done
- Enable the user to set a static IP address
- Create a numpad for the ping interface
- Create a disk image of a minimal RaspberryPi OS-based distro which runs the python app in a kiosk mode (only app at boot)
- Enable the raspberry pi to run as an IPerf server

### Nice to have (maybe will be done, but are not the current focus)
- Make settings persistent between reboots
- More interactivity (screens)
- More beautification (icons, images, fonts)
- Enable the pi to see the public IP address
- Enable the user to connect to wlan
- Log data using PyShark
- See visible hosts on network
- Reference charts (maybe you network engineers can tell me which references you would like to have)
- Network performance graphs (speed, latency...)

### Can you do that? (nice ideas that may require extensive modifications of the OS or may not be possible)
- SSH shell (will need either a virtual or physical keyboard)
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
  It will work but the speed most likely will show 1 Gb/s (but hey, it's a 180$ network analyser, what did you expect).
- Since it is using terminal commands and lookup of specific files (a bit hacky), it will most likely break one day when a update is performed to RaspberryPi OS. But most likely not next week.
- There WILL be some security flaws. It is not intended to be a highly secure device, only a small tool for network enthusiasts. Use it at your own risk.
- May not work on future Pi models.
- On the Raspberry Pi 3, you might not see internet speeds higher that 200Mb/s. This is due to the speed of the integrated NIC. It should go all the way to 1 Gb/s on Pi 4 models.

### Dependencies
- socket
- netifaces
- struct
- subprocess
- speedtest-cli
- tkinter
- time
- threading
  
### Screenshots
![Screenshot_20220130_112321](https://user-images.githubusercontent.com/76972727/151708011-c2393f9e-93dc-4333-b959-beb668515e1f.png)
![Screenshot_20220130_112341](https://user-images.githubusercontent.com/76972727/151708012-71127d59-1efa-4792-9bc7-33fa156a3ecd.png)
![Screenshot_20220130_112413](https://user-images.githubusercontent.com/76972727/151708013-1047f1a5-5f26-473e-98e1-2bf2fc230053.png)
![Screenshot_20220130_112524](https://user-images.githubusercontent.com/76972727/151708014-1b6e847b-3ad3-4556-afcf-78a89e3a6efb.png)

If you want to support the project or have any questions, feel free to send me an email at lavoiesidney@gmail.com
