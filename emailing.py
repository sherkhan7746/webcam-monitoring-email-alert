import os
import smtplib
from email.message import EmailMessage
from io import BytesIO
from PIL import Image

PASSWORD = os.getenv("PASSWORD")
SENDER = "sherkhan1167746@gmail.com"
RECEIVER = "sherkhan1167746@gmail.com"
def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "New Customer showed up!"
    email_message.set_content("Hey, We just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    image_data = BytesIO(content)
    img = Image.open(image_data)
    image_format = img.format
    email_message.add_attachment(content, maintype="image", subtype=image_format)

    gmail = smtplib.SMTP("smtp.gmail.com")
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER,RECEIVER, email_message.as_string())
    gmail.quit()
    print("email function ended")


if __name__ == "__main__":
    send_email("images/19.png")