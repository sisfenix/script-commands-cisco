#!/usr/bin/env python3
import netmiko
import getpass
import os
import csv

#ip_address = input("IP Address: ")
#ssh_username = input("SSH Username: ")
#ssh_password = getpass.getpass('SSH Password: ')

ip_address = os.environ["NETMIKO_IP"]
ssh_username = os.environ["NETMIKO_USER"]
ssh_password = os.environ["NETMIKO_PASS"]


def main():
    ssh_connect = netmiko.ConnectHandler(
        device_type="cisco_ios",
        ip=ip_address,
        username=ssh_username,
        password=ssh_password
    )

    result = ssh_connect.find_prompt() + "\n"
    ssh_connect.send_command("terminal length 0")
    result += ssh_connect.send_command("show ip arp", read_timeout=120)
    
    ssh_connect.disconnect()

    return result

if __name__ == "__main__":
    print(main())
