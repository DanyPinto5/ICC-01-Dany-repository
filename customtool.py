import nmap

nm = nmap.PortScanner()

network_range = "192.168.1.1/24" 

print(f"Scanning {network_range}")

nm.scan(hosts=network_range, arguments='-sn')


for host in nm.all_hosts():
    print(f"IP: {host}")
    print(f"Host: {nm[host].hostname()}")
    print(f"Estado: {nm[host].state()}")
    
    if 'mac' in nm[host]['addresses']:
        print(f"MAC Address: {nm[host]['addresses']['mac']}")
    
