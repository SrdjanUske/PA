import sys

if __name__ == "__main__":
	
	N = 4
	lista_torki = []

	for x in range(0, N):
		print("\n\nTuple number " + str(x + 1) + " ->")
		integer = input("\n\tSet integer: ")
		floating = input("\n\tSet float: ")
		string = input("\n\tSet string: ")

		lista_torki.append((int(integer), float(floating), str(string)))

	print("\n" + "Lista svih torki:\n\t" + str(lista_torki))
	del lista_torki[0]
	print("\n" + "Lista svih torki bez prve:\n\t" + str(lista_torki))