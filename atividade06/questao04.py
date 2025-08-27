import requests

def cotacao_em_real(moeda):
    url = (f'https://economia.awesomeapi.com.br/last/{moeda}-BRL')
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        dados = dados[F'{moeda}BRL']
        print(dados)
        cotacao = (f'{dados['bid']}')
        maxima = (f'{dados['high']}')
        minima = (f'{dados['low']}')
        data = (f'{dados['create_date']}')
        return cotacao, maxima, minima, data

    
    except requests.RequestException as e:
        print(f'erro ao obter a cotação: {e}')
        return None, None, None, None
    
moeda = input('qual moeda você deseja ver a cotação (EUR, USD, GBP): ').upper()
cotacao, maxima, minima, data = cotacao_em_real(moeda)
print(f'{moeda} \nvalor: {cotacao} \nMaxima: {maxima} \nMinima: {minima} \ndata e horario: {data}')