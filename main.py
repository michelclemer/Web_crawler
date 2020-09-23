import nms as nms
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

'''Acessando home  site'''
url = "http://www.nuforc.org/"
page = requests.get(url)
page.encoding = 'utf-8'
#Busca o conteúdo da página
soup = BeautifulSoup(page.text, 'html.parser')
#salva os links na variavel LINK
link = soup.a['href']
#acessa o Link seguinte
html = requests.get(url+link)
#Busca o conteúdo da página
soup2 = BeautifulSoup(html.text, 'html.parser')

''' Busca todo as tags para link'''
links = soup2.find_all('a')

dicionario_datas_links = {}
'''Percorre os links acima'''
for i in links:
    if '1996' in str(i):
       break
    if '.html' and '0' in str(i):
        '''Adiciona a data e link em um dicionário'''
        dicionario_datas_links[i.string] =  i['href']
subpagina = url+'webreports'
'''Entrando no link'''
lista_data_hora = []
'''Percorre  o dicionario'''
for chave, valor in dicionario_datas_links.items():
    html2 = requests.get(subpagina+'/'+valor)
    print('Link ', html2.url, ' - Status: ', html2.status_code)
    lista_data_hora.append(html2.url)
'''Acessando a quarta pagina'''

'''Acessando o link'''

'''ultima pagina'''
link_final = []
url = []
lista = []
cont = 0
for link in lista_data_hora:
    html3 = requests.get(str(link))
    soup3 = BeautifulSoup(html3.text, 'html.parser')
    links = soup3.find_all('a')
    for i in links:
        print(i['href'])
        link_final.append(subpagina+'/'+i['href'])
    links = []
    for i in link_final:
        html4 = requests.get(i)
        soup4 = BeautifulSoup(html4.text, 'html.parser')
        br = soup4.findAll('br')
        for i in br:
            next_s = i.nextSibling
            result = str(next_s).replace('<br/>', '')
            lista.append(result)
        d = pd.DataFrame([lista])
        d.to_csv('log.csv', mode='a', header=False)
        lista = []

