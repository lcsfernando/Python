#Estrutura de repetição, também conhecida como laços de repetição.
#For(para) while(enquanto)
i = int(input('Escolha um número: '))
for n in range(12, 0, -1):
    print(n, 'x', i, '=', (n*i))
x = 1
while x<= 15:
    print(x, 'x', i, '=', (x*i))
    x+=1
if x<=30:
    print(x, 'x', i, '=', (x * i))
    x += 1
def tabuada(i, n, x):
    print(i*n*x)
print(tabuada(i,n,x))