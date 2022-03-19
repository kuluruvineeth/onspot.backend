# mail service for sending email notifications using a google account
import smtplib

# sending an email (accepts recipient email, message and optional subject line
def send_email_spothole(mailToEmail, message, subject="New notification from Onspot!"):
    try:
        gmailaddress = "<YOUR EMAIL ADDRESS HERE>" # EMAIL ADDRESS HERE
        gmailpassword = "<YOUR EMAIL PASSWORD HERE>" # EMAIL PASSWORD HERE
        mailto = mailToEmail
        msg = 'From: Onspot App\nSubject: {}\n\n{}'.format(subject, message)
        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.starttls()
        mailServer.login(gmailaddress, gmailpassword)
        mailServer.sendmail(gmailaddress, mailto, msg)
        mailServer.quit()
        return ("Email Sent")
    except:
        return ("Email Not Sent")
