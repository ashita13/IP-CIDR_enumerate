import ipaddress
import socket
import sys
import nmap
import argparse

# ping sweep using nmap -n -sn flags
def ping_sweep(target):
    print("Performing ping sweep")
    scanner = nmap.PortScanner()
    scanner.scan(hosts=target, arguments='-n -sn')
    up_hosts = []
    for host in scanner.all_hosts():
        if scanner[host].state() == 'up':
            up_hosts.append(host)
    #  write to file 
    for i in up_hosts:
        with open("./ips_sweeped.txt", "a") as file:
            file.write(i + "\n")
        print(i, "Host is alive")

# subnetting function
def subnetting(target):
    try:
        net = ipaddress.ip_network(target, strict=False)
        print(f"Target            : {target}")
        print(f"Network address   : {net.network_address}")
        hosts = list(net.hosts())
        print(f"First host        : {hosts[0]}")
        print(f"Last host         : {hosts[-1]}")
        print(f"Broadcast address : {net.broadcast_address}")
        print(f"Subnet mask       : {net.netmask}")
        print(f"Usable hosts      : {net.num_addresses}")
        if hosts:
            print(f"Host IP range     : {hosts[0]} - {hosts[-1]}")
        else:
            print("No usable host addresses")
    except ValueError:
        print("Invalid IP/CIDR")
        
    
# output
def main():
    parser = argparse.ArgumentParser(description="Network Discovery and Subnetting Tool by ashita13")

    parser.add_argument("-p", "--ping", metavar="TARGET", help="Perform ICMP ping sweep on target")
    parser.add_argument("-s", "--subnet", metavar="TARGET", help="Show subnet information on target")

    args = parser.parse_args()

    if args.subnet:
        target = args.subnet
        subnetting(target)

    if args.ping:
        target = args.ping
        ping_sweep(target)

    if not args.ping and not args.subnet:
        parser.print_help()
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
