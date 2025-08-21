##Importando Lib
from currency_converter import CurrencyConverter
c = CurrencyConverter()

##Recebendo valor do usuario
valor_em_real = float(input("digite o valor em real: "))

##Convertendo valores
valor_em_dolar = c.convert(valor_em_real, 'BRL', 'USD')
valor_em_euro = c.convert(valor_em_real, 'BRL', 'EUR')

##Resultado
print(f"valor em dolar: {valor_em_dolar:.2f} \nvalor em euro: {valor_em_euro:.2f}")