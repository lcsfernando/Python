import math

idade=int(input('Qual sua idade: '))
if idade>=18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')
    '''
    IDENTAÇÃO
    
    É uma forma de arrumar o codigo, fazendo com que algumas linhas fiquem mais à direita que as outras, á medida que adicionamos espaços em seu início.
    A identação é uma caracteristica importante do Python e deve ser respeitado!!! pois é essencial para o funcionamento do código.
    Enquanto na maioria das linguagens de desenvolvimento como, C, Java, JavaScript, PHP, entre outros os blocos são delimitados por chaves. O Python usa blocos para delimitar ou tabular e organizar para o funcionamento e identificação visual
    Neste caso não existe abre e fecha condicional.
    '''
    #a = int(input('Informe um valor para a variavel A: '))
    #b = int(input('Informe um valor para a variavel B: '))
    #total = a+b
'''if a > b:
    print('A é maior que B')
elif a==b:
    print("A igual a b")
else:
    print('B é maior que A')'''
'''while a < b:
    a=a+b
    print('Dentro do loop a = {}'.format(a))
else:
    print(a)'''
'''for total in range(7):
    total=total*2
    print(total)'''
notaA = float(input('Informe sua primeira nota: '))
notaB = float(input('Informe sua segunda nota: '))
media = (notaA+notaB)/2
if media>=5 and media<7:
    print('Você está de reforço, sua média foi de {}.'.format(media))
elif media>=7:
    print('Você foi aprovado, sua média foi de {}.'.format(media))
else:
    print('Você foi reprovado, sua média foi de {}.'.format(media))
