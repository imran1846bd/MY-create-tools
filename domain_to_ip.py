import socket
import pyfiglet
from termcolor import colored

banner=colored(pyfiglet.figlet_format("Domain To IP"),'green')
print(banner)
domain_name=input("Enter teget Domain name to find IP adress: ")

ip=socket.gethostbyname(domain_name)
print("IP For {} :{}".format(domain_name,ip))
