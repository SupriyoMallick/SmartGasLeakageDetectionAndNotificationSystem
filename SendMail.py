"""We start by only importing only the classes we need, this also saves us from
having to use the full module name later."""

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
#Code build by Supriya Mallick - Email ID here.i.am.supriyo@gmail.com
#Then we compose some of the basic message headers:

fromaddr = "Sender Email id"
toaddr = "Recepient Email id"

#msg['Subject'] = "Python email subject"
body = "Python test mail body"
#Next, we attach the body of the email to the MIME message:
def sendEmail(subject,msgBody):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject']=subject
    body=msgBody
    msg.attach(MIMEText(body, 'plain'))

    try:
    #server = smtplib.SMTP('smtp.gmail.com', 587)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login("sender email id", "sender mail password")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)        
        print ("Successfully sent email")
        body=''
    except smtplib.SMTPException:
        print ("Error: unable to send email")
        
#sendEmail("IoT enabled LPG Gas Sensor Test","This a IoT enabled gas sensor testing.")
  