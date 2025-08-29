import csv

def ler_csv(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                print(linha)
    except Exception as e:
        return(f'erro ao ler o arquivo: {e}')
nome_arquivo = 'atividade07/'
nome_arquivo += input('Digite o nome do arquivo: ')
if nome_arquivo[-4:] != '.csv':
    nome_arquivo += '.csv'
ler_csv(nome_arquivo)