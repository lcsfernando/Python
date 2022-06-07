#Game de perguntas e respostas
print('Olá bem vindo ao teste de conhecimento!!!')
inicio = (input('Vamos iniciar o quiz? (s/n) '))
inicio = inicio.upper()
'''while inicio != 'S' and inicio != 'SIM' and inicio != 'YES' and inicio != 'VAMOS' and inicio != 'Y':
    print('Que pena você desistiu sem tentar!')
    inicio = input('Vamos iniciar o quiz? (s/n) ')
    inicio = inicio.upper()
else:
    print('Legal vamos iniciar!!!')'''
if inicio != 'S' and inicio != 'SIM' and inicio != 'YES' and inicio != 'VAMOS' and inicio != 'Y':
    print('Que pena você desistiu antes de tentar!')
    input('Por favor pressione a tecla ENTER para sair.')
    quit()
else:
    print('Legal vamos iniciar!!!')
'''if inicio == 'S' or inicio == 'SIM' or inicio == 'YES':
    print('Legal vamos começar!!')
else:
    print('Que pena desistiu antes de tentar!')'''

input('Por favor pressione a tecla ENTER para continuar')
print('\nPergunta 1:')

pergunta1 = input('Informe a resposta de 10 + 10 = ')
if pergunta1 == '20':
    print('Você acertou, ganhou um ponto')
    pontos = 1
    print('Pontos:', pontos)
else:
    print('Você errou perdeu um ponto')
    pontos = -1
    print('Pontos:', pontos)
print('\nPergunta 2:')

import os
os.system('pause')

pergunta2 = input('Qual a capital de Minas Gerais: ')
pergunta2 = pergunta2.lower()
if pergunta2 == 'belo horizonte' or pergunta2=='bh':
    print('Você acertou, ganhou um ponto')
    pontos += 1
    print('Pontos:', pontos)
else:
    print('Você errou perdeu um ponto')
    pontos -= 1
    print('Pontos:', pontos)
print('\nPergunta 3:')
print('Qual o carro mais conhecido pela cor vermelha')
print('a) Fusca')
print('b) Mercedez')
print('c) Ferrari')
print('d) BMW')
p3 = input('Escolha a alternativa: ')
p3 = p3.lower()
if p3 == 'c':
    print('Você acertou, ganhou um ponto')
    pontos += 1
    print('Pontos:', pontos)
else:
    print('Você errou perdeu um ponto')
    pontos -= 1
    print('Pontos:', pontos)
