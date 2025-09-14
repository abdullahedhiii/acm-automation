import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from emailTemplate import getHtmlContent

SMTP_SERVER = "smtp.gmail.com"    
SMTP_PORT = 587                    
SENDER_EMAIL = "abdullahedhi17@gmail.com"
SENDER_PASSWORD = "ykua xjli janj jsde"  

RECIPIENTS = ["k224575@nu.edu.pk","k224626@nu.edu.pk"]

subject = "ACM Appointment Letter"

html_template = getHtmlContent()


msg = MIMEMultipart()
msg['From'] = SENDER_EMAIL
msg['To'] = ", ".join(RECIPIENTS)  
msg['Subject'] = subject

msg.attach(MIMEText(html_template, "html"))

pdf_filename = "Appointment Letter.pdf"
with open(pdf_filename, "rb") as f:
    pdf_attachment = MIMEApplication(f.read(), _subtype="pdf")
    pdf_attachment.add_header("Content-Disposition", "attachment", filename=pdf_filename)
    msg.attach(pdf_attachment)

try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, RECIPIENTS, msg.as_string())
    server.quit()
    print(" Email sent successfully!")
except Exception as e:
    print(" Error:", e)
