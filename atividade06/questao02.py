import requests

def obter_usuario_aleatorio():
    url = 'https://randomuser.me/api/'
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()['results'][0]
        nome = f'{dados['name']['first']} {dados['name']['last']}'
        email = f'{dados['email']}'
        pais = f'{dados['location']['country']}'
        return nome, email, pais
    except requests.RequestException as e:
        print(f'erro ao obter usuario aleatorio: {e}')
        return None

nome, email, pais = obter_usuario_aleatorio()

print(f'Usuario aleatorio \nNome: {nome} \nEmail: {email} \nPais: {pais}')