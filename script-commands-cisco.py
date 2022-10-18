#!/usr/bin/env python3
import netmiko
import getpass
import os
import csv

#ssh_username = input("SSH Username: ")
#ssh_password = getpass.getpass('SSH Password: ')
#ssh_command = input("Command: ")

ssh_username = os.environ["NETMIKO_USER"]
ssh_password = os.environ["NETMIKO_PASS"]
ssh_command = os.environ["NETMIKO_CMD"]

def main():
    with open("file.txt", "r") as filecsv:
        readerfile = csv.DictReader(filecsv)

        for row in readerfile:
            ssh_connect = netmiko.ConnectHandler(
            device_type="cisco_ios",
            ip=row["ipaddress"],
            username=ssh_username,
            password=ssh_password
            )

            ssh_connect.send_command("terminal length 0")

            result = "IP: " + row['ipaddress'] + " - S/N: " + row['sn'] + "\n"
            result += ssh_connect.find_prompt() + "\n"
            result += ssh_connect.send_command(ssh_command, read_timeout=120)
    
            ssh_connect.disconnect()

            with open("output/" + row['ipaddress'] + ".txt", "w") as fw:
                print(result, file=fw)

if __name__ == "__main__":
    main()
