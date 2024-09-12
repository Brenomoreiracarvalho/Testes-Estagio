dados = [
	{
		"dia": 1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	},
	{
		"dia": 6,
		"valor": 26742.6612
	},
	{
		"dia": 7,
		"valor": 0.0
	},
	{
		"dia": 8,
		"valor": 42889.2258
	},
	{
		"dia": 9,
		"valor": 46251.174
	},
	{
		"dia": 10,
		"valor": 11191.4722
	},
	{
		"dia": 11,
		"valor": 0.0
	},
	{
		"dia": 12,
		"valor": 0.0
	},
	{
		"dia": 13,
		"valor": 3847.4823
	},
	{
		"dia": 14,
		"valor": 373.7838
	},
	{
		"dia": 15,
		"valor": 2659.7563
	},
	{
		"dia": 16,
		"valor": 48924.2448
	},
	{
		"dia": 17,
		"valor": 18419.2614
	},
	{
		"dia": 18,
		"valor": 0.0
	},
	{
		"dia": 19,
		"valor": 0.0
	},
	{
		"dia": 20,
		"valor": 35240.1826
	},
	{
		"dia": 21,
		"valor": 43829.1667
	},
	{
		"dia": 22,
		"valor": 18235.6852
	},
	{
		"dia": 23,
		"valor": 4355.0662
	},
	{
		"dia": 24,
		"valor": 13327.1025
	},
	{
		"dia": 25,
		"valor": 0.0
	},
	{
		"dia": 26,
		"valor": 0.0
	},
	{
		"dia": 27,
		"valor": 25681.8318
	},
	{
		"dia": 28,
		"valor": 1718.1221
	},
	{
		"dia": 29,
		"valor": 13220.495
	},
	{
		"dia": 30,
		"valor": 8414.61
	}
]

valorMin = dados[0]['valor']
valorMax = dados[0]['valor']
valorMedio = 0
i = 0
dia = 0
while i < 30 :
	if dados[i]['valor'] < valorMin and dados[i]['valor'] != 0:
		valorMin = dados[i]['valor']
	if dados[i]['valor'] > valorMax:
		valorMax = dados[i]['valor']
	if dados[i]['valor'] != 0:
		dia = dia + 1
	valorMedio = valorMedio + dados[i]['valor']
	i = i+1

valorMedio = valorMedio/dia
print(f'Menor valor nos dias em que não foram feriado ou final de semana é {valorMin}')
print(f'Maior valor é {valorMax}')
maiorMedia = 0
dias = []
for i in range(0,30):
	if dados[i]['valor'] > valorMedio:
		maiorMedia = maiorMedia + 1
		dias.append(i+1)
print(f'O faturamento foi maior que a média em {maiorMedia} dias.', end=' ')
if len(dias) > 0:
	print('Nos dias', end=' ')
else:
	print('No dia', end=' ')
cont = 0
while cont < len(dias) - 1:
	print(f'{dias[cont]}', end=', ')
	cont = cont + 1
print(f'{dias[cont]}', end=' ')