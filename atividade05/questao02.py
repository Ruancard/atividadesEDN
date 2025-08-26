def eh_palindromo(texto):
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    #invertido = texto_limpo[1:3:2]
    invertido = ''
    for letra in texto_limpo:
        invertido = letra + invertido
    return invertido == texto_limpo
entrada = input("Digite uma frase: ")
if eh_palindromo(entrada):
    print(f'a frase "{entrada}" é um palindromo')
else:
    print(f'a frase "{entrada}" não é um palindromo')