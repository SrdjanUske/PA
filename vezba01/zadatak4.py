
lista = []
m = 100

for x in range(1, m + 1):
	lista.append(x)

print("\nlista = [", end = '')

for x in range(m - 1, -1, -1):
	if not(x == 0):
		print(str(lista[x]) + " ", end = ',')
	else:
		print(str(lista[x]) + "]")