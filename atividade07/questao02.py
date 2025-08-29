import csv
from faker import Faker


def escrever_csv(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['nome', 'idade', 'cidade'])
            for linha in dados:
                escritor.writerow(linha)
            return (f'dados criados com sucesso')
    except Exception as e:
        return(f'erro ao escrever no arquivo: {e}')

nome_arquivo = 'atividade07/'
nome_arquivo += input('Digite o nome do arquivo: ')
if nome_arquivo[-4:] != '.csv':
    nome_arquivo += '.csv'
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
    dados.append([nome[n], idade[n], cidade[n]])

escrever_csv(nome_arquivo, dados)