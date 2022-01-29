import speedtest
import subprocess


def get_internet_speed():
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


test = get_internet_speed()
print(test)