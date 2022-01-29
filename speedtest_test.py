import speedtest
import subprocess


def get_internet_speed():
    result = subprocess.getstatusoutput("ping -c 4 speedtest.com")
    if result[0] != 0:
        return False

    else:
        inter = speedtest.Speedtest()
        down = inter.download()
        up = inter.upload()

        return down, up


test = get_internet_speed()
print(test)