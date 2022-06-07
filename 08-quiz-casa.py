#Game de perguntas e respostas
print('Olá bem vindo ao teste de conhecimento!!!')
nome = input('Qual seu nome? ')
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
    input('Pressione enter para sair')
    quit()
else:
    print('Legal vamos iniciar!!!')
'''if inicio == 'S' or inicio == 'SIM' or inicio == 'YES':
    print('Legal vamos começar!!')
else:
    print('Que pena desistiu antes de tentar!')'''
import os
os.system('pause')
print('\nPergunta 1:')
p1 = input('Informe a resposta de 10 + 10 = ')
while not p1.isnumeric():
    p1 = input('Informe a resposta em números não texto de 10 + 10 = ')
else:
    if p1 == '20':
        print('Você acertou, ganhou um ponto')
        pontos = 1
        print('Pontos:', pontos)
    else:
        print('Você errou perdeu um ponto')
        pontos = -1
        print('Pontos:', pontos)
#dica importar no ínicio do código
import time
os.system('pause')
print('\nPergunta 2:')
p2 = input('Qual a capital de Minas Gerais: ')
p2 = p2.lower()
if p2 == 'belo horizonte' or p2=='bh':
    print('Você acertou, ganhou um ponto')
    pontos += 1
    print('Pontos:', pontos)
else:
    print('Você errou perdeu um ponto')
    pontos -= 1
    print('Pontos:', pontos)
print('\nCarregando Pergunta 3...')
time.sleep(5)
print('\nPergunta 3:')
print('Qual o carro mais conhecido pela cor vermelha?')
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
os.system('pause')
print('\nPergunta 4:')
print('Quem descobriu o brasil?')
print('a) Napoleão Bonaparte')
print('b) Dom Pedro I')
print('c) Cristóvão Colombo')
print('d) Pedro Álvares Cabral')
p4= input('Escolha a alternativa correta: ')
p4 = p4.lower()
if p4 == 'd':
    print('Você acertou, ganhou um ponto')
    pontos += 1
    print('Pontos:', pontos)
else:
    print('Você errou perdeu um ponto')
    pontos -= 1
    print('Pontos:', pontos)
os.system('pause')
print('\nPergunta 5:')
print('Qual o lugar mais alto do mundo?')
print('a) Mauna Kea\nb) Dhaulagiri\nc) Monte Chimborazo\nd) Monte Everest\ne) Empire States')
p5 = (input('Escolha a alternativa correta: '))
p5 = p5.lower()
if p5 == 'd':
    print('Você acertou, ganhou um ponto')
    pontos += 1
    print('Pontos:', pontos)
else:
    print('Você errou perdeu um ponto')
    pontos -= 1
    print('Pontos:', pontos)
print('\nCarregando Pergunta 6...')
time.sleep(5)
print('\nPergunta 6:')
print('O que é mais pesado um quilo de algodão ou um quilo de chumbo?')
print('a) Algodão\nb) Chumbo\nc) Nenhuma das alternativas anteriores')
p6 = (input('Escolha a alternativa correta: '))
p6 = p6.lower()
if p6 == 'c':
    print('Você acertou, ganhou um ponto')
    pontos += 1
    print('Pontos:', pontos)
else:
    print('Você errou perdeu um ponto')
    pontos -= 1
    print('Pontos:', pontos)
input('Pressione enter para prosseguir')
print('\nPergunta 7:')
print('Quanto tempo a terra demora pra dar uma volta em torno dela mesma')
print('a) Uma semana \nb) Um dia\nc) Um mês\nd) Um ano')
p7 = (input('Escolha a alternativa correta: '))
p7 = p7.lower()
if p7 == 'b':
    print('Você acertou, ganhou um ponto')
    pontos += 1
    print('Pontos:', pontos)
else:
    print('Você errou perdeu um ponto')
    pontos -= 1
    print('Pontos:', pontos)
os.system('Pause')
print('\nPergunta 8:')
p8 = input('O que é maior megabyte ou gigabyte: ')
p8 = p8.lower()
if p8 == 'gb' or p8 == 'gigabyte':
    print('Você acertou, ganhou um ponto')
    pontos += 1
    print('Pontos:', pontos)
else:
    print('Você errou perdeu um ponto')
    pontos -= 1
    print('Pontos:', pontos)
print('Pergunta 9 à carregar...')
time.sleep(5)
print('\nPergunta 9:')
print('Qual o nome da quinta filha da mãe de Maria:')
p9 = input('Jana, Jena, Jina, Jona: ')
p9 = p9.lower()
if p9 == 'maria':
    print('Você acertou, ganhou um ponto')
    pontos += 1
    print('Pontos:', pontos)
else:
    print('Você errou perdeu um ponto')
    pontos -= 1
    print('Pontos:', pontos)
print('\nPergunta 10:')
p10 = float(input('Quantos pontos você fez até agora: '))
if p10 == pontos:
    print('Você acertou, ganhou um ponto')
    pontos += 1
    print('Pontos:', pontos)
else:
    print('Você errou perdeu um ponto')
    pontos -= 1
print('Pontos:', pontos)
if pontos >= 6:
    print('Parabéns você foi aprovado, você fez %.0f'%pontos)
elif pontos >= 2:
    print('Você está de reforço, você fez {:.0f}'.format(pontos))
else:
    print('Você foi reprovado, você fez:',pontos,'pontos.' )
input('Pressione enter para conferir suas repostas:')
print('Gabarito:\nPergunta 1: {}\nPergunta 2: {}\nPergunta 3: {}\nPergunta 4: {}\nPergunta 5: {}\nPergunta 6: {}\nPergunta 7: {}\nPergunta 8: {}\nPergunta 9: {}\nPergunta 10: {}'.format(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10))
input('Pressione enter para ver as respostas corretas:')
print('\nRespostas:\nPergunta 1: 20\nPergunta 2: Belo Horizonte\nPergunta 3: C\nPergunta 4: D\nPergunta 5: D\nPergunta 6: C\nPergunta 7: B\nPergunta 8: Gigabyte\nPergunta 9: Maria\nPergunta 10: -9 até 9 depende quantas acertou\n \N{grinning face}')
'''arquivo = open('resultados-quiz.txt','w')
arquivo.close()'''
arquivo = open('resultados-quiz.txt','a')
arquivo.write('\nNome: '+ (str(nome)) + ' - Pontos: ' + (str(pontos)))
arquivo.close()
#arquivo = open('')
os.system('pause')
