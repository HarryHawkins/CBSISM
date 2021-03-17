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

def install_NE(ip, uname,pw,os,rsa):
    ssh = createSSHClient(ip, 22, uname, pw)
    scp = SCPClient(ssh.get_transport())
    #this is important to get the correct system architecure, we are generalising here based on OS
    #could add a field allowing arch selection but this is hard to know for general user
    if os =='PI':
        scp.put('/home/harry/FYP/Solution/CBSISM/configuration/scripts/automationScripts/install-pi.sh', '~/install-NE.sh')
    elif os == 'UB':
        scp.put('/home/harry/FYP/Solution/CBSISM/configuration/scripts/automationScripts/install-amd64.sh', '~/install-NE.sh')
    else:
        scp.put('/home/harry/FYP/Solution/CBSISM/configuration/scripts/automationScripts/install-amd64.sh', '~/install-NE.sh')
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
        stdin, stdout, stderr = client.exec_command('sudo bash ~/install-NE.sh') #why wont this run on ubuntu? maybe the sudo prompt issue?
        for line in stdout:
            print('Output from server ' + line.strip('\n'))
            if "install-done" in line.strip('\n'):
                print("done!")
                client.close()
                return(stdout.readlines(),True)
    return(verified)