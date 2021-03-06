#!/usr/bin/env python3
from email.message import EmailMessage
import os.path
import mimetypes
import smtplib


def generate_email(sender, recipient, subject, body, attachment_path):
    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split("/", 1)

    with open(attachment_path, "rb") as ap:
        message.add_attachment(ap.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=attachment_filename)

    return message


def generate_error_email(sender, recipient, subject):
    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    body = "Please check your system and resolve the issue as soon as possible."
    message.set_content(body)

    return message


def send(message):
    mail_server = smtplib.SMTP("localhost")
    mail_server.send_message(message)
    mail_server.quit()
