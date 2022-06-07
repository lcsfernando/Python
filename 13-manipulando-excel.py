'''
INTERPRETADORES DO PYTHON / BIBLIOTECA

INSTALANDO pandas
O pandas é uma ferramenta de análise e manipulação de dados de código aberto, rápida, poderosa, flexível e fácil de usar. Construída sobre a Linguagem de programação Python.
pandas.pydata.org
Após instalado, precisa ser importado ao código pra uso.
Modo padrão de importação: import pandas as pd
Trabalhando com os arquivos excel em Python
pandas.pydata.org

INSTALAR openpyxl
O pacote openpyxl é para ler e gravar aquivos a partir do Excel 2010, ou seja, .xlsx
A linguagem dessa biblioteca edita o Excel com se fosse usando linguagem VBA

INSTALAR xlrd
O pacote xlrd é para ler e gravar arquivos do Excel mais antigo tipo .xls

EXEMPLO de erro apresentado quando falta um pacote:
ImportError> Missing optional depency 'openpyx1' - use pip or install openpyx1

COMO INSTALAR UM INTERPRETADOR / BIBLIOTECA
Configurar um interpretador Python (configure interpreter)

OBS: As bibliotecas são instaladas por projeto.

Menu File / Settings / Project / Python Interpreter / + adicionar / Pesquisar o nome do pacote/interpretador
'''
import pandas as pd
#Criar uma variável para ler o cominho do arquivo de excel localização
import openpyxl
import xlrd
pasta = pd.read_excel('dados.xlsx')
print(pasta)
print('\n')
#pra ler um dado expecífico, devemos informar a coluno (título) e linha (número)
print(pasta['Produto'][3], '\n')
print(pasta['Unitário'][6], '\n')
#unitMorango = float(pasta['Unitário'][6])
#qtdeMorango = float(pasta['Qtde'][6])
#totalMorango = unitMorango*qtdeMorango
#print(totalMorango)
totalFusca = float(pasta['Total'][1])
print(totalFusca, '\n')
#Para localizar um dado também podemos usar o .loc[linha, coluna]
print(pasta.loc[1, 'Qtde'], '\n')
#p=str(pasta.loc[0, 'Produto'])
#print(p.upper())
#Atualizar dados
pasta.loc[1, 'Qtde'] = 3.49
print(pasta.loc[1, 'Qtde'])
print(pasta)
#O pandas reconhece a planilha do Excel como uma tabela de dados, ou seja, DataFrame (Quadro de Dados) do qual reconhece linhas e colunas.
#Também podemos chamar de séries um array (variedade) ou conjunto de informações, neste caso são as informações de uma coluna.
dados = pd.ExcelFile('dados.xlsx')
#print(dados)
#Link de arquivo
print('\n')
dados = pd.read_excel(dados,'Planilha1')
plan1DF = pd.DataFrame(dados)
print(plan1DF)
print('\n')

print('Total de linhas e colunas:', plan1DF.shape)
print(plan1DF.columns)
#Retorna colunas
#object - Para coleção de propriedades
print(plan1DF.count())
#total de dados não nulos
print(plan1DF.describe())
print('\n')
print(plan1DF.sum())
soma = 'A soma do'
total = 'total'
igual = 'é igual a:'
qtde = 'qtde'
unitario = 'unitário'
maximo = 'O máximo do'
minimo = 'O mínimo do'
media = 'A média do'
print(soma,total,igual,(sum(plan1DF.Total)))
print(soma,qtde,igual,sum(plan1DF.Qtde))
print(soma,unitario,igual,sum(plan1DF.Unitário))
print(maximo,qtde,igual,max(plan1DF.Qtde))
print(maximo,total,igual,max(plan1DF.Total))
print(maximo,unitario,igual,max(plan1DF.Unitário))
print(minimo,qtde,igual,min(plan1DF.Qtde))
print(minimo,unitario,igual,min(plan1DF.Unitário))
print(minimo, total, igual,min(plan1DF.Total))
print(media, total,igual,(plan1DF.Total).mean())
print(media,unitario,igual,(plan1DF.Unitário).mean())
print(media,qtde,igual,(plan1DF.Qtde).mean())
#Erro por conta da coluna de texto
#print(plan1DF.mean())
print('\n',(plan1DF[['Categoria','Total']]))
#exibir mais de uma coluna/Filtro por coluna
#Exibir/Selecionar/Agrupar por Categoria/Soma Total
print('\n',(plan1DF[['Categoria','Total']].groupby('Categoria').sum()))
print('\n',(plan1DF[['Produto', 'Categoria','Total']].groupby(['Produto','Categoria']).sum()))
#Classificação Crescente
print('\n',(plan1DF.sort_values(by='Qtde')))
#Classificação decrescente
print('\n',(plan1DF.sort_values(by='Qtde',ascending=False)))

print('\n',(plan1DF.sort_index(ascending=False)))
print('\n')

print(plan1DF['Categoria'].value_counts())
plan1DF.loc[1,'Unitário'] = 5000
i = 1
j = -1
while i < 8 and j<6:
    j += 1
    i += 1
    plan1DF.loc[j, 'Total'] = '=c'+str(i)+'*d'+str(i)

print(plan1DF)
#Salvar
#plan1DF.to_excel('dadosTeste.xlsx')
plan1DF.to_excel('henrique.xlsx', sheet_name='Planilha1',index=False)
