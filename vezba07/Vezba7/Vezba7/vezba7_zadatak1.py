import math
import time
import random

A = (math.sqrt(5) - 1) / 2

class Data:
	def __init__(self, key = None, literal = None):
		self.key = key
		self.literal = literal

def divisionMethod(key, m):
	return key % m

def multiplicationMethod(key, m):
	global A
	return math.floor(m * ((key*A) % 1))

def universalHashing(key, m, p, a, b):
	return ((a*key + b) % p) % m

def CHAINED_HASH_INSERT(T, x, m, p = None, a = None, b = None):
	if p != None and a != None and b != None:
		h = universalHashing(x.key, m)
	else:
		h = multiplicationMethod(x.key, m)

	for elem in T[h]:
		if elem.key == x.key:
			T[h].remove(elem)
	T[h].append(x)


def CHAINED_HASH_SEARCH(T, k, m, p = None, a = None, b = None):
	if p != None and a != None and b != None:
		h = universalHashing(k, m)
	else:
		h = multiplicationMethod(k, m)

	for e in T[h]:
		if e.key == k:
			return e
	return None

def CHAINED_HASH_DELETE(T, x, m, p = None, a = None, b = None):
	if p != None and a != None and b != None:
		h = universalHashing(k, m)
	else:
		h = multiplicationMethod(k, m)

	T[h].remove(x)

def test(n, p, m):
	hash_table = []
	numbers = random.sample(range(1, n+1), n)
	for i in range(0, m):
		hash_table.append([])
	start = time.clock()
	for num in numbers:
		CHAINED_HASH_INSERT(hash_table, Data(num, str(num)), m)
	end = time.clock() - start

	print("n = " + str(n) + "|p = " + str(p) + "|m = " + str(m) + "|time = " + str(end))


if __name__ == "__main__":
	for n in [10000, 50000, 100000]:
		for p in [23, 9973, 99991]:
			for m in [p, p//2, p//4]:
				test(n, p, m)