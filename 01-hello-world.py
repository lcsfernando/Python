print('Hello World')
#Comentário de linha usando a hashtag
''' Comentário em bloco'''
#filosofia de ZEN do Desenvolvedor do Python.
#import this
import os
'''try:
    n = input('Digite um número: ')
    n = (n.replace(',','.'))
    n1 = str(int(float((n))))
except ValueError:
    try:
        n = input('Digite um número, não uma caractere: ')
        n = (n.replace(',', '.'))
        n1 = str(int(float((n))))
    except ValueError:
        try:
            os.system('pause')
        finally:
            n = input('Diga Adeus: ')
            quit()
document = open('arq-texto.txt','a')
i = 1
document.write(str(n)+' x '+str(i)+' = '+str(n*i))
document.close()'''
'''for ValueError:
    n = input('Digite um número: ')
    n = (n.replace(',', '.'))
    n1 = str(int(float((n))))
else:
    document = open('arq-texto.txt', 'a')
    i = 1
    document.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i))
    document.close()'''
n = input('Digite um número: ')
n1 = (n.replace('.','0'))
n1 = (n1.replace(',','0'))
n= (n.replace(',','.'))
t = int(n.count('.'))
print(n)
while not n1.isdigit() or t>1:
    n = input('Digite um número, não uma caractere: ')
    n = (n.replace(',', '.'))
    n1 = (n.replace('.', '0'))
    n1 = (n1.replace(',', '0'))
    t = int(n.count('.'))
else:
    n = float(n)
    print(n*3,14)