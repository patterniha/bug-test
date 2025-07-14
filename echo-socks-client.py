import socket
import time
import socks

sock = socks.socksocket(socket.AF_INET, socket.SOCK_DGRAM)
sock.set_proxy(proxy_type=socks.SOCKS5, addr="127.0.0.1", port=10808)
sock.settimeout(1)
while True:
    sock.sendto(b"hello", ("127.0.0.1", 8888))
    try:
        data, addr = sock.recvfrom(1024)
        print("client-received:",data, addr)
    except Exception:
        print("no received")
    time.sleep(2)
