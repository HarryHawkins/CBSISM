class hello:
    def __init__(self, username, password, ip):
        self.username = username
        self.password = password
        self.ip = ip
    def show(self):
        print(self.username,self.password,self.ip)
