# Send an email
# Hunter Thornsberry
# hunter@hunterthornsberry.com
# I got almost 100% of this code from a Stack Overflow answer, it's not my own work
# You must save this as sendemail.py and fill in your own username and password

def send_email(recipient, subject, body):
    import smtplib

    gmail_user = 'USERNAME'
    gmail_pwd = 'PASSWD'
    FROM = gmail_user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
    except:
        print "failed to send mail"
