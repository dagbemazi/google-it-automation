#!/usr/bin/env python3
import reports
import emails
import os
from datetime import date

user = os.getenv("USER")


def process_data():
    path = f"/home/{user}/supplier-data/descriptions"
    files = os.listdir(path)
    _name = []
    _weight = []
    for file in files:
        with open(f"{path}/{file}") as f:
            lines = f.read().splitlines()
            name = lines[0].strip('\n')
            weight = lines[1].strip('\n')
            _name.append(f"name: {name}")
            _weight.append(f"weight: {weight}")

    new_data = ""

    for i in range(len(_name)):
        new_data += f"{_name[i]}<br/>{_weight[i]}<br/><br/>"

    return new_data


def main():
    c_date = date.today().strftime("%B %d, %Y")
    title = f"Processed Update on {c_date}"
    info = process_data()
    attachment_path = "/tmp/processed.pdf"

    reports.generate_report(attachment_path, title, info)

    sender = "automation@example.com"
    recipient = f"{user}@example.com"
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email(
        sender, recipient, subject, body, attachment_path)
    emails.send(message)


main()
