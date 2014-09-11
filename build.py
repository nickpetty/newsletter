import smtplib
import time
import markdown2
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if (True):
  import generate

name = time.strftime('%m-%d-%Y')

print 'Opening ' + name +'.txt'
md = open(name + '.txt', 'r').read()

me = "nick@ihackeverything.com"

recipients = []

print 'Opening mailList'
mailList = open('emailList.txt', 'r').readlines()
for email in mailList:
	recipients.append(email.strip('\n'))

#recipients = ['nick@ihackeverything.com']

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "IHackEverything Newsletter - " + time.strftime('%m-%d-%Y')
msg['From'] = me
msg['Bcc'] = ", ".join(recipients)

# Create the body of the message (a plain-text and an HTML version).
text = md
today = time.strftime('%m-%d-%Y')

print 'Converting markdown to html'
html = markdown2.markdown(md)

# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html.encode('utf8'), 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.

pw = raw_input('Enter Password: ')

s = smtplib.SMTP('smtp.live.com', 587)
s.ehlo()
s.starttls()
s.login('nick@ihackeverything.com', pw)

# sendmail function takes 3 arguments: sender's address, recipient's address
# and message to send - here it is sent as one string.
print 'Sending Newsletter'
s.sendmail(me, recipients, msg.as_string())
print 'Done.'
s.quit()