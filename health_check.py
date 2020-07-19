import os
import psutil
import shutil
import socket

def check_cpu_usage():
    """ Returns True if CPU usage is high, false otherwise """
    return psutil.cpu_percent(1) > 80

def check_disk_usage(disk):
    """ Returns True if Disk usage is high, false otherwise """
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free < 20

def check_disk_wrapper():
    """ Returns True if Disk usage is high, false otherwise """
    return check_disk_usage(disk='/')

def check_memory_usage():
    """ Returns True if Memory usage is high, false otherwise """
    mu = psutil.virtual_memory().available
    total = mu / (2 ** 20)
    return total < 500

def check_no_network():
    """ Returns True if it fail to resolve localhost URL """ 
    localhost = socket.gethostbyname("localhost")
    return localhost != "127.0.0.1"

def send_email(subject):
    email = emails.generate_email("automation@example.com", "id@example.com", msg,
                                  "Please check your system and resolve the issue as soon as possible.", "")
    emails.send_email(email)


checks = [
    (check_cpu_usage, "Error - CPU usage is over 80%"),    
    (check_disk_wrapper, "Error - Available disk space is less than 20%"),
    (check_memory_usage, "Error - Available memory is less than 500MB"),
    (check_no_network, "Error - localhost cannot be resolved to 127.0.0.1"),
    ]

everything_ok = True
for check, msg in checks:
    if check():
        print(msg)
        everything_ok = False

    if not everything_ok:
        send_email(msg)
        
    print("Everything is fine")
    sys.exit(0)
    
