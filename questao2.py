numero = int(input('Digite um número: '))

inicial = 0
soma = 1
print(f'{inicial}  {soma}  ', end=' ')
while soma < numero:
    intermediario = inicial
    inicial = soma
    soma = inicial + intermediario
    print(f'{soma}', end=' ')

print('')
if soma == numero:
    print(f'O número {numero} pertence a sequencia de fibonacci')

else:
    print(f'O número {numero} não pertence a sequencia de fibonacci')
