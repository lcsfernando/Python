codigo = 10
salario = 1212
nome = 'Lucas Fernando'
situacao = True

print(codigo)
print(salario)
print(nome)
print(situacao)

#Verificando tipo de dados com type
tipo=type(codigo)
print(tipo)
tipo2=type(salario)
tipo3=type(nome)
tipo4=type(situacao)

print(tipo2)
print(tipo3)
print(tipo4)
total = codigo*salario
print(total)
print('O código é: {}/ O salário é: {}/ Meu nome é: {}/Eu fui contratado? {}'.format(codigo,salario,nome,situacao))

'''
Tipos de dados
Inteiro (int), as váriaveis do tipo (int) são aquelas que armazenam números inteiros 1, 2, 3 e assim por diante.
Real (float), representa números reais com decimais e que possuem sinal de expoente (e ou E)
Booleano (bool), representa valores booleanos que são Verdadeiro (True) e falso (False)
String (str), representa qualquer conjunto de caracteres, desde que estejam entre aspas
'''
