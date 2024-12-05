import os
import subprocess

#port_list = [22,80,8080]
port_list = [7,20,21,22,23,25,53,69,80,88,102,110,135,137,139,143,381,383,443,464,465,587,593,636,691,902,989,990,993,995,1025,1194,1337,1589,1725,2082,2083,2483,2484,2967,3074,3306,3724,4664,5432,5900,6665,6667,6668,6669,6881,6999,6970,8086,8087,8222,9100,10000,12345,27374,31337]
#port_list = [4000]
ip = "localhost"
ip = "192.168.192.33"

def nmap(port,ip):
    #bashCommand = "nmap -p" + str(port) + " " + str(ip)
    bashCommand = "nmap -p" + str(port) + " " + str(ip)
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)


#nmap -p22 localhost

def check_IP(ip):
    bashCommand = "ping -c 1 " + ip
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)

#ping -c 1 localhost

check_IP(ip)

for port in port_list:
    #print(port)
    
    nmap(port,ip)
    #os.system()
print("This line will be printed.")