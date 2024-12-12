""" Conversor de moedas utilizando API """

from requests import get
import json

API = get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
JSON = json.loads(API.content)
lista_moedas = [JSON["USDBRL"]["bid"], JSON["EURBRL"]["bid"], JSON["BTCBRL"]["bid"]]

valor_real = float(input("Quantos Reais você tem? R$ ").strip().replace(',', '.'))

print(f"""
o Valor de {valor_real} em outras moedas é

Dolar: {valor_real / float(lista_moedas[0]):.2f} 
Euro: {valor_real / float(lista_moedas[1]):.2f}
BitCoin: {valor_real / float(lista_moedas[2])}
""")
