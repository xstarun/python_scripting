import http.client
import webbrowser
import smtplib
senders = "tarun.sharma@100percentile.com"
receivers = "paras.jain@100percentile.com,hitesh@100percentile.com"

webbrowser.open_new_tab("cksha.leaplms.in")
c = http.client.HTTPConnection("cksha.leaplms.in")
c.request("HEAD", "")
if c.request  == 301:
  print((c.getresponse().status)) 
message = """From: From tarun <tarun.sharma@.100percentile.com>
To: To "paras.jain@100percentile.com","hitesh@100percentile.com">
Subject: "check for email redirect"""
try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")

  \

