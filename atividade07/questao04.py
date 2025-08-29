import json
from faker import Faker

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados_json = json.load(arquivo_json)
            print(dados_json)
    except FileNotFoundError:
        return(f"Arquivo não encontrado")


def escrever_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            for linha in dados:
                print (linha)
            json.dump(dados, arquivo_json, ensure_ascii = False, indent= 4)
        print(f'Dados salvos em: {nome_arquivo}')
    except Exception as e:
        return(f'Erro ao escrever no arquivo: {e}')
    
nome_arquivo = 'atividade07/'
nome_arquivo += input('Digite o nome do arquivo: ')
if nome_arquivo[-5:] != '.json':
    nome_arquivo += '.json'
numero_linhas = (int(input('Digite o numero de linhas que voce deseja criar: ')) - 1)
fake = Faker('pt_BR')
nome = []
idade = []
cidade = []

for _ in range(numero_linhas):
    nome.append(fake.name())
    idade.append(fake.random_int(min=18, max=65))
    cidade.append(fake.city())

dados = []
for n in range(numero_linhas):
    dados.append({f'Nome' : nome[n], f'Idade' : idade[n], f'Cidade' : cidade[n]})

escrever_json(nome_arquivo, dados)
ler_json(nome_arquivo)