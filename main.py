#Autor rogerio.junior20@outlook.com
#Validador de cartão de credito, valido ou não
#Algoritmo de Luhn - é o algoritmo usado em cartão de credito ou debito.

#Modulos importados
import os

#Função de limpar tela
def tela_limpa():
    x = input('\nDigite enter para continuar')
    os.system('limpo' if os.name == 'posix' else 'cls')


#Função para inserir o numero e validar o cartão
def checar(cartão,comprimento):
    sum = 0
    list = [int(x) for x in cartão]
    second = False
    for i in list:
        if second == True:
            i = i*2
        #para somar os digitos se for maior que 9
        sum += i//10
        sum += i%10
        #Para tornar a condição acima se for verdadeira
        second = not(second)
    if sum%10 == 0:
        return True
    else:
        return False

while(True):
    print('Bem Vindo!!')
    print('Esse programa serve para validar o seu cartão de credito.')
    print('Coloque o número do Cartão de Credito : ',end = '')
    while(True):
        try:
            cartão = int(input())
            break
        except:
            print('Coloque o número do Cartão do Credito : ',end = '')
    cartão = str(cartão)
    cartão = cartão[::-1]
    comprimento = len(cartão)
    condiçao1 = checar(cartão,comprimento)
    condiçao2 = True if comprimento == 16 else False
    
    #Checar cartão de aeroporto
    if cartão.endswith('1' or '2') and condiçao1:
        print('\n\nEsse cartão é valido!\nCartão usado para Aeroportos')
    
    #Checar cartão se for da American Express
    elif cartão.endswith('3') and  comprimento == 15 and condiçao1:
        print('\n\nEsse cartão é valido!\nPara entreterimento e viajar\nCartao pertence a American Express')
        
    #Checar cartão se for da Visa
    elif cartão.endswith('4') and condiçao1 and condiçao2:
        print('\n\nEsse cartão é valido!\nCartão de Banco\nO cartão é Visa,Usado para Debito e Credito')
        
    #Checar cartão da Mastercard
    elif cartão.endswith('5') and condiçao1 and condiçao2:
        print('\n\nEsse é cartão é valido!\nCartão de Banco\nCartão da Mastercard,Usado para Debito e Credito')
        
    #Checar algoritmo de Luhn
    elif condiçao1:
        print('\n\nEsse número segue o algoritmo de Luhn, mas não é um cartão de Debito ou Credito')
        
    #O numero não é valido
    else:
        print('\n\nO número do cartão não é valido!\nOu você colocou o número errado')
        

    print('\n\nDeseja colocar outro número (S/N) : ',end = '')
    if input().lower() == 'S' :
        tela_limpa()
        pass
    else:
        break