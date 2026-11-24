import socket

target = input("Enter target IP address (e.g., 127.0.0.1): ")
print(f"Scanning target: {target}...")

# Common ports to check: FTP(21), SSH(22), HTTP(80), HTTPS(443)
ports = [21, 22, 80, 443]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: Closed")
    s.close()
