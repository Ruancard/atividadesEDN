import requests

def consultar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        logradouro = (f'{dados['logradouro']}')
        bairro = (f'{dados['bairro']}')
        cidade = (f'{dados['localidade']}')
        estado = (f'{dados['estado']}')
        return logradouro, bairro, cidade, estado
    
    except requests.RequestException as e:
        print(f'erro ao obter Cep: {e}')
        return None

cep = input('Digite o Cep: ')
logradouro, bairro, cidade, estado = consultar_cep(cep)
print(f'Endereço \nLogradouro: {logradouro} \nBairro: {bairro} \nCidade: {cidade} \nEstado: {estado}')