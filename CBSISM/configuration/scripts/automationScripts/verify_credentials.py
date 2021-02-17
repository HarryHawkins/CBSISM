#take a IP, username and ssh key/pw and verify credentials and connection
#http://www.paramiko.org/
#https://hackersandslackers.com/automate-ssh-scp-python-paramiko/
import base64
import paramiko
def login_test(ip, uname,rsa):
    key = paramiko.RSAKey(data=base64.b64decode(bytes(rsa,'utf-8'))) #replace the string with the actual key - remove before git commit!! 
    client = paramiko.SSHClient() # must be added to known hosts!!
    client.get_host_keys().add(ip, 'ssh-rsa', key)
    client.connect(ip, username=uname, password='password') #my test pi
    stdin, stdout, stderr = client.exec_command('whoami') #should return pi
    for line in stdout:
        print('Output from server ' + line.strip('\n'))
    client.close()

login_test("192.168.0.50","pi","RSA-KEY-HERE") #should print username on endpoint