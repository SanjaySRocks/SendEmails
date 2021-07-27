import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "thisismyemail@gmail.com"

password = input("Sender Email Password & Press Enter : ")
message = """\
Subject: Account Verification

Hi please verify your acccount, if verified please ignore.
"""

with open('emails.txt','r') as file:
    rec_emails = file.readlines()
    print("---------------------")
    print(rec_emails)
    print("---------------------")


context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()

    try:
        server.login(sender_email, password)
        for email in rec_emails:
            try:
                server.sendmail(sender_email, email, message)
                print(f"{email} email sent... ")
            except Exception as e:
                print(e)
                print(f"{email} email send failed ")
    except Exception as e:
        print(e);

    