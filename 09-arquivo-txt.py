#TRABALHANDO COM ARQUIVO TXT
'''
r           Abre o arquivo somente para leitura. O arquivo já deve existir.
r+          Abre p arquivo para leitura e escrita. O arquivo já deve existir (Cria ou reescreve no arquivo existente a partir             da primeira linha e apaga tudo para reescrever)
w           Abre o arquivo somente para escrita, no início do arquivo. Apagará o conteúdo do arquivo se ele já existir. Criára            um novo arquivo se ele ainda não existir.
w+          Abre o arquivo para escrita e leitura, apagando conteúdo preexistente.
a           Acrescentar - Abre ou cria o arquivo para escrita no final. Não apaga o conteúdo preexistente.
a+          Abre o arquivo para escrita e leitura. Não apaga o conteúdo preexistente.

FUNÇÃO open(), após a declaração da variável que receberá a função, necessita de dois parâmetros: o nome do arquivo e depois o modo de como abrir esse arquivo

Sintaxe: arquivo = open('arquivo.txt','w')

FUNÇÃO  white(), é utilizada para gravar informações em um arquivo existente.
Sintaxe: arquivo.write('Aula prática de Python')

FUNÇÃO close(), encerrar o arquivo após sua utilização. IMPORTANTE: Nunca abra 2x antes de fechar!!!!

FUNÇÃO read(), leitura de_todo_conteúdo_do_arquivo
Sintaxe: leitura=open('arquivo.txt')
         print(leitura.read())
         leitura.close()
'''
'''
arquivo = open('arq-texto.txt','w')
arquivo.write('Curso de Python\nAula prática Python')
arquivo.close()
leitura = 
''''''
leitura = open('arq-texto.txt','r')
print(leitura.read())
leitura.close()'''
'''arquivo = open('arq-texto.txt','a')
arquivo.write('Curso de Python com lógica de programação.\n')
#arquivo.close()
print(valores[0])
for valor in valores:
    arquivo.write(str(valor))
arquivo.close()''''''
valores = (100,200,300,400,500,550,690,800,1000)
with open('arq-texto.txt','w') as arquivo:
    for valor in valores:
        arquivo.write('('+str(valor)+')-')
    arquivo.write('\n' + str(valores[5]))
arquivo.close()
abrir = open('arq-texto.txt','a')
abrir.write('\n' + str(valores[5]))
print("\N{grinning face}")
abrir.close()''''''
valores = (100,200,300,400,500,550,690,800,1000)
with open('arq-texto.txt','a') as arquivo:
    arquivo.write('\n')
    for valor in valores:
        arquivo.write('('+str(valor)+')-')
    arquivo.write('\n' + str(valores[5]))
arquivo.close()'''
'''valores = (100,200,300,400,500,550,690,800,1000)
with open('arq-texto.txt','r') as arquivo:
    for valor in arquivo:
        print(valor)
arquivo.close()'''
with open('arq-texto.txt','r+') as arquivo:
    for valor in arquivo:
        print(valor)
    arquivo.write('1997')
arquivo.close()