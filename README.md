# EtherView
Last updated feb 13, 2022.

## Welcome to the EtherView project!

This is a project to transform a RaspberryPi into a portable network diagnostic machine.

The goal of this project is to make a custom Linux distro to enable basic network diagnostic using a RaspberryPi with a touchscreen.
I do not know how long I will maintain this project or how many bugs I will fix. I just want it to run.

The upcoming Linux distro will be based on RaspberryPi OS Lite and will launch a custom python application 
which will enable connectivity tests without the use of a keyboard.

This program can be used on any Linux machine, but not on MacOS or Windows. There will be no ports to these systems, 
since the application is designed to work on a Raspberry Pi running Linux. If you want to use it, go to line 21 and change "bond0" 
to whatever your network interface is. This will be set to eth0 (the Pi's wired interface) in the final release.

### Hardware
The hardware will be a RaspberryPi 3 or 4, with the official touchscreen. A case will also be used to improve ruggedness, but is optional.
The main goal would be to run the Pi and screen on a battery, be it a USB power bank or an integrated lithium battery and charger.

### Currently done
- Full GUI interface
- Obtain status of network interface(up/down)
- Obtain basic network information (IPv4 address, netmask, default gateway, public IP) on a DHCP enabled network.
- Ping a host using IPv4 address.
- Check DNS connectivity
- Test link speed of network interface and internet speed using Ookla's Speedtest
- Can connect to iperf3 servers and do a speed test
- Reload DHCP configuration
- App can be forced to fullscreen
- Pop-ups alert the user if something is wrong
- Working progress bar for long requests
- Clock
- Basic settings menu (for interface, number of ping and host to check DNS)

### To be done
- Enable the user to set a static IP address (close but not quite there yet)
- Create a disk image of a minimal RaspberryPi OS-based distro which runs the python app in a kiosk mode (only app at boot)

### Nice to have (maybe will be done, but are not the current focus)
- Make settings persistent between reboots
- More interactivity (screens)
- More beautification (icons, images, fonts)
- Enable the user to connect to wlan
- Log data using PyShark
- Network performance graphs (speed, latency...)

### Can you do that? (nice ideas that may require extensive modifications of the OS or may not be possible)
- Log network traffic
- View VLANS
- Check cable length
- Check cable wiring (maybe using a USB ethernet dongle or the GPIO pins)
- Serial port

### Known limitations
- Since the interface on the Raspberry is only gigabit, it may not be possible to test faster networks. 
  It will work but the speed most likely will show 1 Gb/s (but hey, it's a 180$ network analyser, what did you expect).
- Since it is using terminal commands and lookup of specific files (a bit hacky), it will most likely break one day when a update is performed to RaspberryPi OS. But most likely not next week.
- There WILL be some security flaws. It is not intended to be a highly secure device, only a small tool for network enthusiasts. Use it at your own risk.
- May not work on future Pi models.
- On the Raspberry Pi 3, you might not see internet speeds higher that 200Mb/s. This is due to the speed of the integrated NIC. It should go all the way to 1 Gb/s on Pi 4 models.

### Dependencies
#### Python
- socket
- netifaces
- struct
- subprocess
- speedtest-cli
- tkinter
- time
- threading
- os

#### Linux
- iperf3

### Screenshots
![Screenshot_20220131_200048](https://user-images.githubusercontent.com/76972727/151898156-7d86c1b1-c0a8-44a6-b55f-056ca4cbb55c.png)
![Screenshot_20220131_200142](https://user-images.githubusercontent.com/76972727/151898160-3eb3ebaf-c17f-46c1-9f9c-7afd95c7d27a.png)
![Screenshot_20220131_200202](https://user-images.githubusercontent.com/76972727/151898161-90983a9b-33d5-4613-a603-e7ccc88a7543.png)
![Screenshot_20220131_200249](https://user-images.githubusercontent.com/76972727/151898164-3a8dec54-2e00-4c95-bc74-64f729dee39e.png)

If you want to support the project or have any questions, feel free to send me an email at lavoiesidney@gmail.com
