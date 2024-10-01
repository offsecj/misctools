import re
import subprocess

# Run masscan on target IP range with -oX xml output

# Define the masscan output file and the single Nmap output file
masscan_file = 'target_masscan.xml'  # Replace with your actual file name
nmap_output_file = 'target_masscan_open.nmap'  # Output file for all Nmap results

# Read the masscan output from the file
with open(masscan_file, 'r') as file:
    masscan_output = file.read()

# Extract IPs and ports
hosts = re.findall(r'<host.*?<address addr="(.*?)".*?<port protocol="tcp" portid="(.*?)".*?</port>', masscan_output, re.DOTALL)

# Construct and execute Nmap commands
for ip, port in hosts:
    nmap_command = f"nmap -Pn -T4 -v -p {port} --open -sC -sV {ip} >> {nmap_output_file}"
    print(f"Executing: {nmap_command}")  # Print the command for verification
    subprocess.run(nmap_command, shell=True)

print(f"Nmap scan results have been saved to {nmap_output_file}.")