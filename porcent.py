import requests
from bs4 import BeautifulSoup
import pandas as pd
lista_data_hora = 'http://www.nuforc.org/webreports/ndxe202009.html'


html4 = requests.get(lista_data_hora)
soup4 = BeautifulSoup(html4.text, 'html.parser')
tag = soup4.find_all('td')
texto = []
contt = 1
result = []
for i in tag:
    print()
    if contt <= 7:
        texto.append(i.get_text())
        contt += 1
    else:
        result.append(texto)
        contt = 1
        texto = []



escreve = pd.DataFrame(result)
escreve.to_csv('log.csv', index=False, sep=',')







