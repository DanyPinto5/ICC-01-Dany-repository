import nmap

nm = nmap.PortScanner()

network_range = "192.168.1.1/24" 

output_file = "customtool.txt"

print(f"Scanning {network_range}")

nm.scan(hosts=network_range, arguments='-sn')

with open(output_file, "a") as file:
    file.write(f"scanning {network_range}\n\n")
    
    for host in nm.all_hosts():
        ip = host
        hostname = nm[host].hostname()
        state = nm[host].state()
       
    #print on terminal
for host in nm.all_hosts():
    print(f"IP: {host}")
    print(f"Host: {nm[host].hostname()}")
    print(f"Estado: {nm[host].state()}")
    
        #save files 
    with open(output_file, "a") as file:
        #file.write(f"scanning {network_range}\n\n")
        file.write(f"IP: {host}\n")
        file.write(f"Host: {nm[host].hostname()}\n")
        file.write(f"Estado: {nm[host].state()}\n")