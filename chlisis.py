import random
import socket
class app4app():
    def __init__(self):
        self.adderr = ''
        self.co = None
        self.daataa = ''

    def pritf(self):
        print("lajsdhfollp")

    def labebel(self):
        eks = random.randint(0, 9)
        return eks

    def start_connection(self):
        while True:
            global teksock
            teksock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ipp = socket.gethostbyname(socket.gethostname())
            teksock.bind((ipp, 9090))
            teksock.listen(1)
            ip, addr = teksock.accept()
            while True:
                if ip:
                    self.adderr = addr[0]
                    self.co = True
                    self.daataa = ip.recv(1024).decode()
                else:
                    self.co = None
