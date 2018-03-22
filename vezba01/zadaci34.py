import sys

N = len(sys.argv)

if N == 1:

	string1 = "srdjan"
	string2 = "usorac"

elif N == 2:

	string1 = sys.argv[1]
	string2 = "usorac"

elif N == 3:

	string1 = sys.argv[1]
	string2 = sys.argv[2]

combine = 2 * string1[0:3] + " " + string2[len(string2) - 3:]
print("Combination: " + combine)

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