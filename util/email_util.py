import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from util import file_util
from config import EMAIL_SMTP_SERVER


def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path):
    # compose email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    # attach file
    part = MIMEApplication(file_util.read(attachment_path,"rb"), Name = attachment_path.split('/')[-1])
    part['Content - Disposition'] = f'attachment; filename="{attachment_path.split("/")[-1]}"'
    msg.attach(part)
    # Connect to SMTP server
    try:
        server = smtplib.SMTP(EMAIL_SMTP_SERVER, 25)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print(f"Email sent successfully to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        # Close the server connection
        if server:
            try:
                server.quit()  
            except Exception as e:
                print(f"Failed to close the server connection: {e}")
                
