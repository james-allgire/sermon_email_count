import pandas as pd
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

#Add a header so we can read values from the csv file
Cov = pd.read_csv("test_csv.csv", 
                  sep='\t', 
                  names=["Counts"])

# %Y%m%d gives us a 4 digit year 2020 two digit month 01 and two digit day 01
now = datetime.now()
day_month_year = now.strftime("%d/%m/%Y")

# Set up all of the varialbe to pull the numbers from the csv file
sunday_school_total = Cov['Counts'][0]
sunday_school_peak = Cov['Counts'][1]
sunday_am_total = Cov['Counts'][2]
sunday_am_peak = Cov['Counts'][3]
sunday_pm_total = Cov['Counts'][4]
sunday_pm_peak = Cov['Counts'][5]
wed_total = Cov['Counts'][6]
wed_peak = Cov['Counts'][7]

#print(wed_total)
#print(wed_peak)
#email setup
# gmail account used to send text messages
from_email = "fbcmonitoring@gmail.com"
pas = "tuktaj-hazdax-vydSy3"

sms_gateway = 'jamesallgire@icloud.com' #13174373889@tmomail.net' # Email or Mobile numbers that we send email/text messages to 
# The server we use to send emails in our case it will be gmail but we can use others 
smtp = "smtp.gmail.com" 
port = 587 # Port used by the email provider.

# This will start our email server
server = smtplib.SMTP(smtp,port)
# Starts the email server
server.starttls()
# Now we need to login
server.login(from_email,pas)

# Use the MIME module to structure our message.
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = sms_gateway
# Add a new line in the subject
msg['Subject'] = "Livestream Counts"
# Add new lines to your body
body = f"Danielle,\nHere are the livestream counts for the week of: {day_month_year}\nSunday School\n	Total - {sunday_school_total}\n	Concurrent - {sunday_school_peak}\n\nSun AM\n	Total - {sunday_am_total}\n   Concurrent - {sunday_am_peak}\n\nSun PM\n   Total - {sunday_pm_total}\n	Concurrent - {sunday_pm_peak}\n\nWed\n	Total - {wed_total}\n	Concurrent - {wed_peak}\n\nFBC Media Team"
# Attach text so we can send html content.
msg.attach(MIMEText(body, 'plain'))

sms = msg.as_string()

server.sendmail(from_email,sms_gateway,sms)

# lastly quit the server
server.quit()

