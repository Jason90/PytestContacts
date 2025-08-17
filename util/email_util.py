import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from util import file_util


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
        server = smtplib.SMTP('smtp.sohu.com', 25)
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
    
def send1(sender_email, receiver_email, password, subject, body):
    # compose email content
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] =subject
    message.attach(MIMEText(body, "plain"))

    # Connect to SMTP server
    smtp_server = "smtp.sohu.com"
    smtp_port = 25
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)

        # Send email
        server.sendmail(sender_email, receiver_email, message.as_string())
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
                
