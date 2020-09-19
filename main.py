import requests
from bs4 import BeautifulSoup
import pandas as pd

'''Acessando home  site'''
url = "http://www.nuforc.org/"
page = requests.get(url)
page.encoding = 'utf-8'
soup = BeautifulSoup(page.text, 'html.parser')
'''Acessando segunda pagina'''
link = soup.a['href']

html = requests.get(url+link)

soup2 = BeautifulSoup(html.text, 'html.parser')

'''Acessando terceira pagina'''
links = soup2.find_all('a')

dicionario_datas_links = {}
for i in links:
    if '1996' in str(i):
       break
    if '.html' and '0' in str(i):
        dicionario_datas_links[i.string] =  i['href']
subpagina = url+'webreports'
'''Entrando no link'''
lista_data_hora = []
for chave, valor in dicionario_datas_links.items():
    html2 = requests.get(subpagina+'/'+valor)
    print('Link ', html2.url, ' - Status: ', html2.status_code)
    lista_data_hora.append(html2.url)
'''Acessando a quarta pagina'''

'''Acessando o link'''

'''ultima pagina'''
csv_file = {}
result = []
texto = []
for link in lista_data_hora:
    html3 = requests.get(str(link))
    soup3 = BeautifulSoup(html3.text, 'html.parser')
    links = soup3.find_all('a')
    for i in links:
        print(i['href'])
        lista_data_hora.append(subpagina+'/'+i['href'])
    links = []
    for i in lista_data_hora:
        html4 = requests.get(i)
        soup4 = BeautifulSoup(html4.text, 'html.parser')
        tag = soup4.find_all('td')
        for i in tag:
            links.append(i)
            #file = open('saida.txt', 'w')
            for i in links:

                #file.write(i.get_text())
                #file.write("\n")
                texto.append(i.get_text())

            result.append(texto)
            texto = []
            print("Adicionando")
            print()
            print(result)
            print()


        print('-----------------')

        print('ESCREVENDO')

        print('-----------------------')
        escrever_csv = pd.DataFrame(result)
        escrever_csv.to_csv('log.csv', index=False, sep=',')

        print('-----------------')

        print('ESCREVENDO')

        print('-----------------------')



            #file.close()
