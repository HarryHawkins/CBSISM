#take a IP, username and ssh key/pw and verify credentials and connection
#http://www.paramiko.org/
#https://hackersandslackers.com/automate-ssh-scp-python-paramiko/
import base64
import paramiko
from scp import SCPClient


def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def login_test(ip, uname,pw,rsa):
    ssh = createSSHClient(ip, 22, uname, pw)
    scp = SCPClient(ssh.get_transport())
    scp.put('/home/harry/FYP/Solution/CBSISM/configuration/scripts/automationScripts/install.sh', '/home/pi/install.sh')
    verified = False
    key = paramiko.RSAKey(data=base64.b64decode(bytes(rsa,'utf-8'))) #RSA public key ssh_host_rsa_key.pub
    client = paramiko.SSHClient() # must be added to known hosts!!
    client.get_host_keys().add(ip, 'ssh-rsa', key)
    client.connect(ip, username=uname, password=pw) 
    stdin, stdout, stderr = client.exec_command('whoami') 
    for line in stdout:
        if line.strip('\n')==uname:
            verified = True
            print("Connection and credentials verified")
    if verified:
        print("installing node")
        stdin, stdout, stderr = client.exec_command('sudo bash /home/pi/install.sh') 
        for line in stdout:
            print('Output from server ' + line.strip('\n'))
            if "LICENSE" in line.strip('\n'):
                print("done")
                client.close()
                return(stdout.readlines())
    return(verified)
    
# login_test("192.168.0.50","pi","password","AAAAB3NzaC1yc2EAAAADAQABAAABAQC1VrjntLv0+sH0VVU6rKlqwIW7a1AJdpMklYwKNesFtne3a0uKJ1FRbmyCcJUchZ4ByS1pjZZ4oKs/YMGpEXoxgJuuCo/RQjiCMbmY4PkdQ1egwNI/3ej4ELE5T9xgzrzg3F6XLIIXZTXbZfZeB82tydhnL+mk39/6OZbpo5IShiAg1HWs4Sdsbi5GBumD75rkLqBYwMf4t5syiIn804waRZExBPrkqMaRhI6W/H+bSEuvGhRtZG6V6XwdMUcC36Kgyjstjhq6zto4pkkrP28VR/AQL3aziir6NWC72NHVwQ027tMWfZlgJQuEuqf8U80ETq7t/EXVvjn6aE0fc1RB") #should print username on endpoint
