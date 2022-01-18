import pandas as pd
import smtplib

SenderAddress = "musharafpes2021@gmail.com"
password = "Sahidha@12"

e = pd.read_excel('Email.xlsx', engine='openpyxl')
#e = pd.read_excel("Email.xlsx")
emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
msg = "Result arrived, Click the link to check results ..."
subject = "RESULT_ALERT!!!"
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()