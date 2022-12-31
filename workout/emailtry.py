import smtplib
import datetime

date = datetime.datetime.now().strftime( "%d/%m/%Y %H:%M" )
msg = f"From: max.karamurzin@gmail.com\nTo: kennywebber@outlook.com\nSubject: Subject\nDate: {date}\n\nPython" % ()
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("max.karamurzin@gmail.com", "jnbsxtcgqfdallgq")
server.sendmail("max.karamurzin@gmail.com", "kennywebber@outlook.com", msg)
server.quit()