"""
Given a string. The task is to check if the given string is IPv4 or IPv6 or Invalid.

Examples:

Input : “192.168.0.1”
Output : IPv4
Explanation : It is a valid IPv4 address

Input : “2001:0db8:85a3:0000:0000:8a2e:0370:7334”
Output : IPv6
Explanation : It is a valid IPv6 address

Input : “255.32.555.5”
Output : Invalid
Explanation : It is an invalid IPv4 address as the 3rd octet value(i.e 555) is greater 255.

Input : “250.32:555.5”
Output : Invalid
Explanation : The given string is invalid as it consists of both : and .
"""
from ipaddress import ip_address, IPv4Address

def validIPAddress(IP: str) -> str:
    try:
        return "IPv4" if type(ip_address(IP)) is IPv4Address else "IPv6"
    except ValueError:
        return "Invalid"


Ip = "192.168.0.1"
print(validIPAddress(Ip)) 
  
Ip = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
print(validIPAddress(Ip)) 
  
Ip = "256.32.555.5"
print(validIPAddress(Ip))  
  
Ip = "250.32:555.5"
print(validIPAddress(Ip))
        