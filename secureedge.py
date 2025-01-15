import nmap

nm = nmap.PortScanner()

network_range = "192.168.1.1/24" 

output_file = "customtool.txt"

print(f"Scanning {network_range}")

nm.scan(hosts=network_range, arguments='-sn')

#with open(output_file, "w") as file:
    #file.write(f"scanning {network_range}\n\n")
       

for host in nm.all_hosts():
    print(f"IP: {host}")
    print(f"Host: {nm[host].hostname()}")
    print(f"Estado: {nm[host].state()}")
    

with open(output_file, "w") as file:
    file.write(f"scanning {network_range}\n\n")
    file.write(f"IP: {host}")
    file.write(f"Host: {nm[host].hostname()}")
    file.write(f"Estado: {nm[host].state()}")
with open(output_file, "w") as file:
    file.write(f"scanning {network_range}\n\n")
    file.write(f"IP: {host}")
    file.write(f"Host: {nm[host].hostname()}")
    file.write(f"Estado: {nm[host].state()}")


    #if 'mac' in nm[host]['addresses']:
        #print(f"MAC Address: {nm[host]['addresses']['mac']}")