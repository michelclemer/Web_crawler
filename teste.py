import requests
from bs4 import BeautifulSoup
import pandas as pd
file = open('saida.txt', 'r')
lista = []


for i in file:
    lista.append(i)
print(lista)
