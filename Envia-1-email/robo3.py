from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests

response = requests.get('http://api.github.com/users/paulo')
data = response.json()

# Atribuição de variáveis
email = 'rpacurso@gmail.com'
senha = 'curso123456'
destinatario = 'roboparapython@gmail.com'
assunto = 'Informações recebidas via API GitHub'
mensagem = 'Dados do usuário:\n Nome: %s\n Seguidores: %s\n Seguindo: %s\n' % (
    data['name'], data['followers'], data['following'])

print('Iniciando nosso robo...')

path = '/home/kellina/Projetos/Robos/chromedriver'
driver = webdriver.Chrome(path)
driver.get('http://www.gmail.com')

print('Realizando login....')
login = driver.find_element_by_id('identifierId')
login.clear()
login.send_keys(email)
login.send_keys(Keys.RETURN)
time.sleep(2)

password = driver.find_element_by_name('password')
password.clear()
password.send_keys(senha)
password.send_keys(Keys.RETURN)
time.sleep(2)
print('Login realizado!')

print('Abrindo caixa de escrever email...')
driver.get('https://mail.google.com/mail/u/0/#inbox?compose=new')
time.sleep(3)

para = driver.find_element_by_name('to')
para.send_keys(destinatario)
para.send_keys(Keys.RETURN)

subject = driver.find_element_by_name('subjectbox')
subject.send_keys(assunto)
subject.send_keys(Keys.RETURN)

body = driver.find_element_by_xpath('//div[@aria-label="Message Body"]')
body.send_keys(mensagem)

enviar = driver.find_element_by_xpath(
    '//div[@aria-label="Send ‪(Ctrl-Enter)‬"]')
enviar.click()
print('E-mail enviado com sucesso!')
time.sleep(3)

driver.close()
