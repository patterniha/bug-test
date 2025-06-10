# send udp b"1" with socks5 


import socket
import socks

sock = socks.socksocket(socket.AF_INET, socket.SOCK_DGRAM)
sock.set_proxy(proxy_type=socks.SOCKS5, addr="127.0.0.1", port=10808)
sock.sendto(b"1", ("example.com", 1000))
