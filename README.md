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
- Pop-ups alert the user if something is wrong

### To be done
- Enable the user to set a static IP address
- Complete the GUI, make it prettier
- Add more settings to the menu
- Create a numpad for the ping interface
- Create a disk image of a minimal RaspberryPi OS-based distro which runs the python app in a kiosk mode (only app at boot)

### Nice to have (maybe will be done, but are not the current focus)
- Clock
- More interactivity (loading bars, screens)
- More beautification (icons, images, fonts)
- Enable the pi to see the public IP address
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
  
### Screenshots
![Screenshot_20220129_214230](https://user-images.githubusercontent.com/76972727/151684722-a19f0f87-8696-4ad8-b6fe-719e2a470be4.png)
![Screenshot_20220129_214252](https://user-images.githubusercontent.com/76972727/151684723-55d21d81-355e-40cf-8c46-2435cc41da6b.png)
![Screenshot_20220129_214339](https://user-images.githubusercontent.com/76972727/151684724-49b405dc-9581-444b-a4d0-b1bf404dfdbc.png)
![Screenshot_20220129_214422](https://user-images.githubusercontent.com/76972727/151684725-75b443f1-c8f1-4b15-bf93-981241b35425.png)

If you support the project or have any questions, feel free to send me an email at lavoiesidney@gmail.com
