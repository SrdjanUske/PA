import sys

file_name = "dict_test.txt"

while True:

	rec = input("\nUnesite rec (ili pritisnite enter za kraj programa): ")

	if rec == "":
		print("\nKRAJ PROGRAMA")
		break

	count = 0

	if len(sys.argv) > 1:
		file_name = sys.argv[1]

	file_input = open(file_name, "r")

	source = ""
	words = []
	dictionary = {}

	source = file_input.read()

	#print(source)
	source = source.replace("\n", " ")
	words = source.split(" ")

	for x in range(0, len(words)):
		if words[x].find(".") != -1 or words[x].find(",") != -1:

			words[x] = words[x][:-1]

	#for x in range(0, len(words)):
	#	print(words[x], end= " ")

	for x in range(0, len(words)):
		if words[x] in dictionary:
			dictionary[words[x]] += 1

		else:
			dictionary[words[x]] = 1


	if rec in dictionary:
		count = dictionary[rec]

	print("Rec se ponavlja " + str(count) + " puta u recniku.")