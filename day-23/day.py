import ipaddress
import socket
import sys

address = input(f"\nEnter ip address: ")

try:

    ip = ipaddress.ip_address(address)
    print(ip, "is a valid ip address.")

except ValueError:
    print("Invalid ip address!")
    sys.exit()
    
hostname = input(f"\nEnter hostname: ").strip()

try:

    address = socket.gethostbyname(hostname)
    print(f"{hostname} resolves to {address}.")

except socket.gaierror:
    print("Hostname does not resolve to any address!")

    sys.exit()

while True:
    try:

        port_number = int(input(f"\nEnter port number: "))

        if 1 <= port_number <= 65535:
            break

        else:
            print("Enter a port number between 1 and 65535!")

    except ValueError:
        print("Enter a whole number!")
     
try:

    with socket.create_connection((str(ip), port_number), timeout=3):
        pass

except OSError:
    print("Connection failed!")
    

else:
    print("Connection is successful.")


