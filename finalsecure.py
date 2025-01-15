import nmap

nm = nmap.PortScanner()

network_range = input("Please, Insert Ip and CIDR block : ") 
#cidr = input("Please, insert CIDR Block : ")

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


###########################################
#|      Script created by Dcman          |#
###########################################