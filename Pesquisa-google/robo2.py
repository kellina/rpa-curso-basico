from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

pesquisa = input('Digite a pesquisa: ')

path = '/home/kellina/Projetos/Robos/chromedriver'
driver = webdriver.Chrome(path)
driver.get('https://www.google.com')
search = driver.find_element_by_name('q')
search.send_keys(pesquisa)
search.send_keys(Keys.RETURN)
time.sleep(2)
resultados = driver.find_element_by_id('result-stats').text
print(resultados)

num_resultados = int(resultados.split('Aproximadamente ')[1].split(' resultados')[0].replace('.', ''))
# cada pagina tem 10 elem
num_max_pag = num_resultados/10
pags_percorrer = int(input('\n%s páginas encontradas. \nAté qual página quer ir? ' % (num_max_pag)))

url_pag = driver.find_element_by_xpath('//a[@aria-label="Page 2"]').get_attribute('href')
pag_atual = 0
start = 10
lista_resultados = []

while pag_atual <= pags_percorrer - 1:
  if not pag_atual > 0:
    url_pag = url_pag.replace('start=%s' % start, 'start=%s' % (start + 10))
    start += 10
  elif pag_atual == 1:
    driver.get(url_pag)
  pag_atual += 1

  # Pegar os elementos: titulo e o link de cada resultado
  divs = driver.find_elements_by_class_name('g')
  for div in divs:
    nome = div.find_element_by_tag_name('h3').text
    link = div.find_element_by_tag_name('a').get_attribute('href')
    resultado = '%s; %s' % (nome, link)
    print (resultado)
    lista_resultados.append(resultado)

# criar e abrir um arquivo txt
with open('resultados.txt', 'w') as arquivo:
  for resultado in lista_resultados:
    arquivo.write('%s\n' % resultado)
  arquivo.close()

print('%s resultados encontrados do google e salvos no arquivo' % len(lista_resultados))

driver.close()

