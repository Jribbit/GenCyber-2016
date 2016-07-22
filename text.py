import smtplib

while True:

    to = '8482194611@tmomail.net'
    
    gmail_user = "goannabananasavana@gmail.com"
    gmail_pwd = "U7CWbg4wJkrmXB"
    
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user,gmail_pwd)
    
    header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: HEY \n'
    print(header)
    msg = header + '\n HELOOOOO \n\n'
    smtpserver.sendmail(gmail_user, to, msg)
    print('Done!')
    smtpserver.close()
