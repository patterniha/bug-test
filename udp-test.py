import socket
import time


for j in range(1000):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(b"123", ("2.2.2.2", 443))
    print("sent", j+1)
    time.sleep(.001)


