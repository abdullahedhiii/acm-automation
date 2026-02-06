import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from dotenv import load_dotenv
from gen_pdf import generate
import datetime
from email.message import EmailMessage


# Load environment variables
load_dotenv()
senderEmail = os.getenv("SENDER_EMAIL")
senderPassword = os.getenv("SENDER_PASSWORD")

def signIn():
    """Logs into the SMTP server and returns the session."""
    smtp_server = "smtp.gmail.com"
    try:
        smtp = smtplib.SMTP(smtp_server, 587)
        smtp.starttls()
        smtp.login(senderEmail, senderPassword)
        # print("[+] Signed in successfully!")
        return smtp  
    except smtplib.SMTPAuthenticationError:
        print("[X] Authentication error: Check email/password.")
    except smtplib.SMTPConnectError:
        print("[X] Connection error: Unable to connect to SMTP server.")
    except Exception as e:
        print(f"[X] Error: {e}")
    return None

# def sendEmailContent(recieverEmail, subject, htmlContent, name):
#     """Sends an email with HTML content and an optional PDF attachment."""
#     smtp = signIn()
#     if not smtp:
#         print(f"[X] SMTP sign-in failed. Email to {recieverEmail} not sent.")
#         return False

#     try:
#         msg = MIMEMultipart("related")
#         msg["From"] = senderEmail
#         msg["To"] = recieverEmail
#         msg["Subject"] = subject

#         msg.attach(MIMEText(str(htmlContent), 'html'))

#         with open(r"C:\Users\ABC\Documents\acm-automation\images\final.png", "rb") as f:
#             img = MIMEImage(f.read())
#             img.add_header("Content-ID", "<image1>")
#             img.add_header("Content-Disposition", "inline", filename=f"Appointment_Letter_{name}.png")
#             msg.attach(img)

#         smtp.sendmail(senderEmail, recieverEmail, msg.as_string())
#         smtp.quit()
#         print(f"[+] Email sent successfully to {recieverEmail}")
#         return True

#     except smtplib.SMTPRecipientsRefused:
#         print(f"[X] Invalid email address: {recieverEmail}. Saving to unsent list.")
#         return False
#     except Exception as e:
#         print(f"[X] Error sending email: {e}")
#         return False
    

def sendEmailContent(name, comp, recieverEmail, subject, htmlContent, attachment=None):
    
    smtp = signIn()
    if not smtp:
        print(f"[X] SMTP sign-in failed. Email to {recieverEmail} not sent.")
        return False

    try:
        # Create a multipart message
        msg = EmailMessage()
        msg["From"] = senderEmail
        msg["To"] = recieverEmail
        msg["Subject"] = subject
        generate(name, comp)


        with open(attachment, "rb") as content_file:
            content = content_file.read()
            msg.add_attachment(
                content, maintype="application", subtype="pdf", filename=attachment.split('/')[-1]
            )

        # Attaching the email design
        emailBody = MIMEText(htmlContent, "html")

        msg.attach(emailBody)


        # Send email
        smtp.sendmail(senderEmail, recieverEmail, msg.as_string())
        smtp.quit()
        print(f"[+] Email sent successfully to {recieverEmail}")
        return True

    except smtplib.SMTPRecipientsRefused:
        print(f"[X] Invalid email address: {recieverEmail}. Saving to unsent list.")
        return False
    except Exception as e:
        print(f"[X] Error sending email: {e}")
        return False
