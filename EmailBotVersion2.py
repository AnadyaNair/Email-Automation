# github.com/AnadyaNair
# this email bot can send automatic email!
# there are some important requirements for this email bot, got to https://github.com/AnadyaNair/AnadyaNair_auto-email_bot/blob/main/email-requirements.md

import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

constants = "email_address", "subject", "message"
 
def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print("you said: ",info)
            return info.lower()
    except:
        pass

def send_email(reciever, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    code = "SENDER'S PASSWORD"
    server.login('SENDER-S EMAIL ADDRESS', code)
    email = EmailMessage()
    email['From'] = 'SENDER-S EMAIL ADDRESS'
    email['To'] = reciever
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'CONTACT1' : 'CONTACT-S EMAIL ADDRESS',
    'CONTACT2' : 'CONTACT-S EMAIL ADDRESS',
    'CONTACT3' : 'CONTACT-S EMAIL ADDRESS'
}


def get_email_info():
    talk('To whom you want to send email?')
    name = get_info()
    reciever = email_list[name]
    print("The email reciever is: ", reciever)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell the message, please.')
    message = get_info()

    send_email(reciever, subject, message)


get_email_info()
