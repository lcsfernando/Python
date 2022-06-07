import os
texto = 'Manipulação de textos no Python'
print(texto)
'''#ANÁLISE
print(len(texto))
#conta caracteres mais espaços
print(texto.count('o'))
#conta caracter específico
print(texto.count('o', 11, 31))
#conta de o caracter de um determinado ponto até outro ponto
print(texto.find('n',23,31))
#conta do 0 até onde está a caracter inicial do que procura
print(texto.find('qwe'))
#não encontrou retorna -1
print('Python' in texto)
#retorna valor booleano se o conjunto de caracters está no texto'''
''''#TRANSFORMAÇÃO
print(texto.replace('Python', 'Cobra'))
print(texto)
texto = (texto.replace('Python', 'Cobra'))
print(texto)
#Exercício: Substituir na entrada de texto um valor com vírgula para valor com ponto ao fazer a leitura.
num = input('Digite um valor decimal: ')
num = num.replace(',','.')
num=float(num)
print(num)
print(type(num))
print(texto.upper())
print(texto.lower())
print(texto.capitalize())
print(texto.title())
textoEspaco = '   Texto com espaços     '
print(textoEspaco)
print(textoEspaco.strip())
num=input('Digite um numero')
num = num.replace(',','.')
print(textoEspaco.lstrip())'''
print(texto.split())
#dividir a variável em lista por palavra
'''num=input('Digite um valor')
num1=num.replace(',','.')

while not num1.isnumeric():
    num=input('Digite um numero não um caracter')
    num1 = num.replace(',', '.')
else:
    num=num.replace(',','.')
    num=float(num)'''
print('-'.join(texto))
print(texto[5])
print(texto[7:19:2])
print(texto[:7])
print(texto[7:])
print(texto[7::3])
