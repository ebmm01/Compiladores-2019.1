import os
import smtplib
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("kingschool.agenda@gmail.com", "Kingschool123")

msg = MIMEMultipart('alternative')
msg['Subject'] = 'Kingschool'
msg['From'] = 'administrativo@kingschool.com.br'
msg['To'] = 'brunomatiascasas@hotmail.com'

email_content = MIMEText('<html><body> '+
'<img src="cid:image0">' +
'<p>testeeeeeeeeeeeeee</p>' +
'<img src="cid:image1">' +
'</body></html>', 'html', 'utf-8')
msg.attach(email_content)

header = MIMEImage(open('./img/header.png', 'rb').read())
header.add_header('Content-ID', '<image0>')
msg.attach(header)

footer = MIMEImage(open('./img/footer.png', 'rb').read())
footer.add_header('Content-ID', '<image1>')
msg.attach(footer)

server.sendmail(msg['From'], [msg['To']], msg.as_string())
server.quit()

print('funfou')
