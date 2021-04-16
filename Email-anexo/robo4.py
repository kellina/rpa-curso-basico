from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import smtplib # usada para enviar e-mails (simples ou com anexo)

# instancia do objeto de mensagem
msg = MIMEMultipart()

# imagem como anexo
anexo = 'kellina.jpg'

# parametros da mensagem
password = 'curso123456'
mensagem = 'E-mail enviado com um anexo pelo robô usando biblioteca smtplib.'
fromaddress = 'rpacurso@gmail.com'
toaddress = 'rpacurso@gmail.com, kellina@gmail.com, paulosales@gmail.com'
msg['From'] = fromaddress
msg['To'] = toaddress
msg['Subject'] = 'E-mail de teste2'

# add corpo da mensagem
msg.attach(MIMEText(mensagem, 'plain'))

# enviando imagem no corpo da mensagem
file = open(anexo, 'rb')
img = MIMEImage(file.read())
file.close()
img.add_header('Content-ID', '<{}>'.format(anexo))
msg.attach(img)

# criando servidor
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# credenciais de login para enviar o email
server.login(msg['From'], password)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print ("E-mail enviado com sucesso para %s:" % (msg['To']))

#############################
# Anexando arquivo PDF

# filename = 'arquivo.pdf'
# anexo = open('arquivo.pdf', 'rb')
# p = MIMEBase('application', 'octet-stream')
# p.set_payload((anexo).read())
# encoders.encode_base64(p)
# p.add_header('Content-Disposition', 'attachement; filename-%s' % filename)
# msg.attach(p)