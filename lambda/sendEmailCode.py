import json

import boto3, os, json
import smtplib
import email.message
from boto3.dynamodb.conditions import Key, Attr

url_expiration = 172800 # 2days

def sendEmail(to, subject, body):

    gmail_sender =
    gmail_passwd =

    USERNAME_SMTP =
    PASSWORD_SMTP =

    HOST = "email-smtp.us-east-1.amazonaws.com"
    PORT = 587

    print(gmail_passwd)
    msg = email.message.Message()
    msg['Subject'] = subject
    msg['From'] = gmail_sender
    msg['To'] = to
    msg.add_header('Content-Type','text/html')
    msg.set_payload(body)

    # Gmail Sign In

    server = smtplib.SMTP(HOST, PORT)
    server.ehlo()
    server.starttls()
    server.login(USERNAME_SMTP, PASSWORD_SMTP)
    server.login(gmail_sender, gmail_passwd)

    print(msg)
    try:
        server.sendmail(gmail_sender, [to], msg.as_string())
        print ('email sent to ' + to)
    except:
        print ('error sending mail to ' + to)

    return server.quit()

def lambda_handler(event, context):

    for record in event['Records']:
        payload=record["body"]
        print(payload)
        payload = json.loads(payload)

        if payload["token"] == "12345":
            to = payload["to"]
            subject = payload["subject"]
            body = payload["body"]
            sendEmail(to, subject, body)

    return "done"

