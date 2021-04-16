import smtplib  # usada para enviar e-mails (simples ou com anexo)
import email.message
from html import html_email

password = 'curso123456'
msg = email.message.Message()
msg['From'] = 'rpacurso@gmail.com'
msg['To'] = 'rpacurso@gmail.com, kellina@gmail.com, paulosales@gmail.com'
msg['Subject'] = 'Email Newsletter2'
msg.add_header('Content-Type', 'text/html')
msg.set_payload(html_email)

# criando servidor
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# credenciais de login para enviar o email
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print("E-mail enviado com sucesso para %s:" % (msg['To']))
