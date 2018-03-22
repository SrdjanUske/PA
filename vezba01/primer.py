import sys

if len(sys.argv) > 1:
	ime_liste = sys.argv[1]

else:
	ime_liste = "ime_liste"

lista = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

recnik = {ime_liste : lista}

print(str(recnik))