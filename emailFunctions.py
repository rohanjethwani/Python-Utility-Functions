import os
import smtplib
# Below import is dependent on fileFunctions.py present in same repository
import fileFunctions as fileFunc

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

def sendMail(emailDL, subject, **kwargs):
    attachment = krawgs.get("attachment", None)
    body = kwargs.get("body", "")
    doZIP = kwargs.get("doZIP", None)
    
    SUBJECT = subject
    FILENAME = os.path.basename(attachment)
    FILEPATH = os.path.dirname(attachment)
    FROM_EMAIL = "fromEmailID.github.com"
    TO_EMAIL = emailDL
    SMTP_SERVER = "addSmtpServerName"
    
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL
    msg['Subject'] = SUBJECT
    msg.attach(MIMEText(body, "plain"))
    
    if doZIP == 'Y':
        fileFunc.compressFileInZip(attachment)
        FILENAME = FILENAME + ".zip"
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(os.path.join(FILEPATH, FILENAME), "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', filename = FILENAME)
    msg.attach(part)
    
    smtpObj = smtplib.SMTP(SMTP_SERVER)
    smtpObj.sendMail(FROM_EMAIL, [email_id.strip() for email_id in TO_EMAIL.split(",")], msg.as_string())
    print("Email sent successfully")
    smtpObj.quit()
    
    #delete temp zip files
    if doZIP == 'Y':
        fileFunc.silentDelete(os.path.join(FILEPATH, FILENAME))


                   
    
    
    
