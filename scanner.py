#Coded By ysufkibar / cybreex
# .-. coding:utf-8 .-.

import os
import sys
import time
import pyfiglet
import socket

os.system("apt-get install pyfiglet")

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)
print("""
----------------------------------
|Developer: ysufkibar / cybreex  |
----------------------------------
|Instagram: @ysufkibar / @cybreex|
----------------------------------
""")
site = input("Target: ")
target = socket.gethostbyname(site)

print("-" * 50)
print("Target Scanning: " + target)
print("-" * 50)

try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if (result == 0):
            print("Port {} open".format(port))
        s.close()
except Exception as e:
    print("Error!", e)

