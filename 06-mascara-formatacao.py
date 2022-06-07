'''
FORMATAÇÃO DE MÁSCARA
Assim como em outras linguagens, é possível utilizar identificadores para representar os tipos de dados armazaenados nas variáveis que devem ser exibidas na tela.
o Python utiliza a formatação comum entre várias linguagens de desenvolvimento para as máscaras.
Exemplo na tabalea abaixo de Máscara, Tipo de Dados e Descrição:

%d ou %i                 Int (inteiro)                   Exibe um valor inteiro.
%f                       Float ou double                 Exibe um valor decimal.
%id                      Long Int                        Exibe um número inteiro longo.
%e ou  %E                Float e double                  Exibe um número exponencial (número científico)
%c                   Char (caractere)                    Exibe um caractere
%o                       int                             Exibe um número inteiro em formato octal.
%x ou %X                 int                             Exibe um número inteiro no formato hexadecimal.
%s                       Char                            Exibe uma cadeia de caracteres (string).
%r                       Boolean                         Exibe True ou False.
Vide exemplos abaixo aplicação:
'''

fruta = 'Laranja'
print(fruta)
print('Meu suco favorito é de: {}'.format(fruta))
print('Meu suco favorito é de', fruta)
print('Meu suco favorito é de... '+ fruta)
print('Suco de %s é o meu favorito'%fruta.upper())
#Exiba a mensagem suco de laranja é meu favorito, amo laranja.
print('Suco de %s é meu favorito,'%fruta, 'amo %s.'%fruta)
print('Suco de %s é meu favorito, amo %s.'%(fruta,fruta))
print('Suco de {} é meu favorito!'.format(fruta))
cor = ['Azul','Vermelha','Prata']
print('Gosto do céu {}, a flor {} e para o carro prefiro {}.'.format(cor[0],cor[1],cor[2]))
print('Suco de {0} é meu favorito, amo {0}.'.format(fruta))
conta=10/3
print('O valor da conta é %.2f'%conta)
print('O valor da conta é {:.2f}'.format(conta))
