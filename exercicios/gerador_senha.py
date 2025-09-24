# 1 - Escreva um programa que gere uma senha aleatória com um determinado comprimento. A senha deve conter uma mistura de letras, números e caracteres especiais. O comprimento da senha deve ser fornecido pelo usuário. Se o comprimento for menor que 4, imprima uma mensagem de erro e peça ao usuário para fornecer um novo comprimento.

    ## - A senha deve ser aleatória, então cada vez que o usuário executar o programa, uma nova senha deve ser gerada. Obrigatoriamente, a senha deve conter pelo menos uma letra, um número e um caractere especial. A senha não pode conter espaços em branco.

    ### - O programa deve conter uma função chamada `gerar_senha` que recebe o comprimento da senha como parâmetro e retorna a senha gerada. Se o comprimento for inválido, a função deve retornar None.

#Exemplo de saída:


#Digite o comprimento da senha: 10
#8Zn$*2q9X

#- Dica: use a biblioteca random e a função shuffle para embaralhar os caracteres da senha.
#- Dica: use a função choice, dessa mesma biblioteca, para escolher um caractere aleatório de uma string.
#- Dica: use a biblioteca string para obter uma lista de caracteres válidos para a senha.

import random, string

def gerar_senha():
    while True:
        try:
            tamanho=int(input('Digite a quantidade de caracteres desejado para a senha: '))
            if tamanho < 4:
                print('-'*86)
                print('Senha mmuito curta, a senha deve ter pelo menos 4 digitos, Digite novamente o tamanho!'.upper())
                print('-'*86)
                continue
        except ValueError:
            print('-'*41)
            print('Voce digitou uma letra, digite um numero!'.upper())
            print('-'*41)
            continue
        else:
                senha=[
                    random.choice(string.ascii_letters), # Escolhe um caracter de letra maiúscula ou minúscula
                    random.choice(string.digits), # escolha um caracter de numero
                    random.choice(string.punctuation), # Escolhe um caracter de pontuação especial
                ]
                possibilidades="".join([string.ascii_letters,string.digits,string.punctuation]) #Usando uma variavel para juntar todos os tipos de caracteres possivel para a senha, usando join para fazer essa junção, transformando de lista para string
                senha.extend(random.choices(possibilidades, k=tamanho -3 )) #Criando uma extençãa na lista de senha, adicionando os caracteres que faltam na senha, diminuindo 3 pois ja foram passados na lista 

                random.shuffle(senha) # embaralha os caracteres 
        return ' '.join(senha) # join é um metodo de string, recebe uma lista como parametro e retorna uma string

print(gerar_senha())
