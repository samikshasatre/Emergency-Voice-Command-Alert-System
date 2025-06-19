import smtplib
from email.message import EmailMessage

def send_email(image_path, location):
    msg = EmailMessage()
    msg['Subject'] = '🚨 Emergency Alert Triggered!'
    msg['From'] = 'satresamiksha@gmail.com'
    msg['To'] = 'mssatresamiksha3345@gmail.com'
    msg.set_content(f"Emergency triggered.\nLocation: https://maps.google.com/?q={location[0]},{location[1]}")

    with open(image_path, 'rb') as f:
        msg.add_attachment(f.read(), maintype='image', subtype='jpeg', filename='scene.jpg')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('satresamiksha@gmail.com', 'kkzh zyik axbm jmqy')
        smtp.send_message(msg)
