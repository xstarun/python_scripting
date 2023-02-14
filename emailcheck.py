#import smtplib


"""
fromaddr = 'tarun.sharma@100percentile.com'
toaddrs  = 'xstarun@gmail.com'
msg = 'Why,Oh why!'
username = 'tarun sharma'
password = 'ggn@1234'
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit() """

# ==========================================================================================
#!/usr/bin/python


import smtplib

sender = 'tarun.sharma@100percentile.com'
receivers = ['xstarun@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")
