from config import SERVER_MAIL_ADDRES, SERVER_MAIL_PASSWORD
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText

from_addr = SERVER_MAIL_ADDRES
my_pass = SERVER_MAIL_PASSWORD

def send_message(dest_addr, head, body):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = dest_addr
    msg['Subject'] = head

    msg.attach(MIMEText(body, 'html'))
    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(from_addr, my_pass)
    text = msg.as_string()
    server.sendmail(from_addr, dest_addr, text)
    server.quit()   

send_message("npnbem.fm@gmail.com", "Your Personal Travel Assistent", """
Hello! I found out everything at your request: that means recording on
Treatment of hemorrhoids is carried out on Fridays from 9:00 room No. 12
Have with you:
- clean panties;
— Vaseline “Good Wizard” or “Wet Bunny”;
— surgical gloves size 7;
- money (750 rub.)
Sorry for writing on the wall, I have something
PM slows down and don't say thank you...
Always happy to help, bro.""")