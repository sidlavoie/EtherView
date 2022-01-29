import subprocess
ping_host = 'google.com'
ping = subprocess.getstatusoutput("ping -c 10 " + ping_host)
if ping[0] == 0:
    print("Sucess!")
else:
    print("Failure!")
print(ping[1])
