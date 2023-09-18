
#iip = ""
#teksock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#ipp = socket.gethostbyname(socket.gethostname())

#teksock.bind((ipp, 6))
#print('i hear yoiu ')
#teksock.listen(10)
#ip, addr = teksock.accept()

#print(ip, addr)

import socket
import datetime
import time

ip = socket.gethostbyname(socket.gethostname())

ketofshock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        ketofshock.connect((ip, 9090))
        if ketofshock != None:
            break
    except ConnectionRefusedError:
        print("sapp")
        continue

while True:
    curr_ent_time = datetime.datetime.now()
    timetobesentiguess = curr_ent_time.strftime("%X")
    pugrade = timetobesentiguess.encode()
    ketofshock.sendall(pugrade)









