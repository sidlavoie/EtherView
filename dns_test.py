import subprocess

def check_dns(host):
    print("Checking DNS. May take a minute...")
    result = subprocess.getstatusoutput("ping -c 1 " + host)
    if result[0] == 0:
        return True

    else:
        return False


dns=check_dns("google.com")

if dns is True:
    print("Fonctionne")

else:
    print("Fonctionne pas")