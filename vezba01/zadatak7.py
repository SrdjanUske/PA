import sys

if __name__ == "__main__":
	
	N = 4
	lista_setova = []

	for x in range(0, N):
		print("\n\nTuple number " + str(x + 1) + " ->")
		integer = input("\n\tSet integer: ")
		floating = input("\n\tSet float: ")
		string = input("\n\tSet string: ")

		lista_setova.append({int(integer), float(floating), str(string)})

	print("\n" + "Lista svih setova:\n\t" + str(lista_setova))
	del lista_setova[0]
	print("\n" + "Lista svih setova bez prvog:\n\t" + str(lista_setova))