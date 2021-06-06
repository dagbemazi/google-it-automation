#!/usr/bin/env python3

import psutil
import shutil
import socket
import sys
import smtplib
import os
from emails import generate_error_email, send


def network_check():
    url = "localhost"
    try:
        response = socket.gethostbyname(url)
        return False
    except:
        return True


def disk_usage():
    du = shutil.disk_usage("/")

    free = (du.free / du.total) * 100
    return free < 20


def cpu_check():
    usage = psutil.cpu_percent(interval=1)
    return usage > 80


def memory_usage():
    THRESH_HOLD = 500 * 1024 * 1024
    mem = psutil.virtual_memory()
    return mem.available < THRESH_HOLD


def main():
    checks = [
        (disk_usage, "Error - Available disk space is less than 20%"),
        (network_check, "Error - localhost cannot be resolved to 127.0.0.1"),
        (cpu_check, "Error - CPU usage is over 80%"),
        (memory_usage, "Error - Available memory is less than 500MB")
    ]
    everything_ok = True
    user = os.getenv("USER")

    sender = "automation@example.com"
    recipient = f"{user}@example.com"
    for check, msg in checks:
        if check():
            print(msg)
            mail = generate_error_email(sender, recipient, msg)
            send(mail)

            everything_ok = False

    if not everything_ok:
        sys.exit(1)


main()
