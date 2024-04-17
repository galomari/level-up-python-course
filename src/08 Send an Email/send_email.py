import smtplib ,ssl
def email_sender(sender_email,receiver_email,message):
    port=465
    password=input("type your own password")
    stmp_server="smtp.gmail.com"
    context=ssl.create_default_context
    message = message

    with smtplib.STMP_SSL(stmp_server,port,context=context) as server:
        server.login(sender_email,password)
        server.sende_email(sender_email,receiver_email,message)
        


# commands used in solution video for reference
if __name__ == '__main__':
    # replace receiver email address
    email_sender('RECEIVER@EMAIL.COM', 'Notification', 'Everything is awesome!')
