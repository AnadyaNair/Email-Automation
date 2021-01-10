# github.com/AnadyaNair
# this email bot can send automatic email!
# there are some important requirements for this email bot, got to https://github.com/AnadyaNair/AnadyaNair_auto-email_bot/blob/main/email-requirements.md
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
passpasscode = "SENDER'S PASSWORD" # for security purpose, the passcode has to be a variable.
server.login('SENDER'S EMAIL ADDRESS', passpasscode)
server.sendmail('SENDER'S EMAIL ADDRESS', 
    'RECIEVER'S EMAIL ADDRESS',
    'EMAIL CONTENT, i.e. Hi! The auto email bot works!')
             
