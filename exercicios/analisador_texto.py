import string # muito utiil para lidar com strings para tratamentos de texto
from collections import Counter # utilizado para obter um contador de palavras e letras 


# 1 - Crie um programa que analise um texto fornecido pelo usuário. O programa deve contar o número de palavras (independentemente se há repetição ou não), a quantidade de cada palavra e a quantidade de cada letra. Ignore maiúsculas e minúsculas ao contar letras (ou seja, transforme tudo para minúsculas). Faça o devido tratamento para pontuação e espaços ao contar palavras.

    ## - O programa deve conter uma função chamada `analisar_texto` que recebe o texto como parâmetro e retorna a contagem de palavras, a frequência de palavras e a frequência de letras. A função deve ser devidamente documentada.
    
#Para o texto =  "Olá mundo! Este é um teste. Olá novamente." o programa deve imprimir:

    ## - Contagem de palavras: 8
    ## - Frequência de palavras: Counter({'Olá': 2, 'mundo': 1, 'Este': 1, 'é': 1, 'um': 1, 'teste': 1, 'novamente': 1})
    ## - Frequência de letras: Counter({' ': 7, 'e': 6, 'o': 4, 't': 4, 'm': 3, 'n': 3, 'l': 2, 'á': 2, 'u': 2, 's': 2, 'd': 1, 'é': 1, 'v': 1, 'a': 1})

def analisar_texto(texto):
    """
    Analisa o texto passado como parâmetro, realiza o tratamento para remover pontuações, calcula a contagem de palavras ignorando repetições se ouver, calcula a frequência com que as palavras aparecem e calcula a frquência com que as letras aparecem no texto, ignorando maiúsculas e minúsculas.
    
    parametros
    ----------
    texto : str
        texto a ser analisado
    return
    ------
    tupla
        contagem de palavras, frequência de palavras, frequência de letras
    
    """
    tratamento= str.maketrans('','', string.punctuation) # maktrans serve para fazer eventuais substituições e dizer oque é para remover, no caso aqui apenas está removendo as pontuações usando "string.punctuation" para remover as pontuações do texto 
    texto_tratado=texto.translate(tratamento)
    #contagem das palavras
    palavras=texto_tratado.split() # split realioza a contagem de palavras de um texto
    cont_palavras=len(palavras)
    
    freg_palavras=Counter(palavras)
    
    freg_letras=Counter(texto_tratado.lower())
    
    
    return cont_palavras, freg_palavras, freg_letras


#programa principal
texto=input('digite seu texto: ')
cont_palavras, freg_palavras, freg_letras=analisar_texto(texto)

print(f'contagem de palavras é : {cont_palavras}\nfrequencia de palavras é: {freg_palavras}\nfrequencia de letras é : {freg_letras}')