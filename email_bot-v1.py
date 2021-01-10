import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
passpasscode = "SENDER'S PASSWORD"
server.login('SENDER'S EMAIL ADDRESS', passpasscode)
server.sendmail('SENDER'S EMAIL ADDRESS', 
    'RECIEVER'S EMAIL ADDRESS',
    'EMAIL CONTENT, i.e. Hi! The auto email bot works!')
