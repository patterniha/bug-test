import socket
import time

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 1234))
time.sleep(1)
s.close()
