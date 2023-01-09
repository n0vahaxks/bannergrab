import os

def banner_grab(ip_address):
    # Use Nmap to perform banner grabbing
    command = "nmap -sV -p 22 --script=banner " + ip_address
    process = os.popen(command)
    results = str(process.read())
    return results

# Test the banner_grab function
print(banner_grab("8.8.8.8"))

