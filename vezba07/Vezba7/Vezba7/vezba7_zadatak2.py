import math
import time
import random

c1 = 1 / 2
c2 = 1 / 2

h = None

class Data:
	def __init__(self, key = None, literal = None):
		self.key = key
		self.literal = literal

def firstHashFunc(key, m):
	return key % m

def secondHashFunc(key, m):
	return 1 + (key % (m - 1))

def linearProbing(key, i, m, h, hd = None):
	return (h(key, m) + i) % m

def quadraticProbing(key, i, m, h, hd = None):
	global c1, c2
	return (h(k, m) + c1*i + c2*i*i) % m

def doubleHashing(key, i, m, h1, h2):
	return (h1(key, m) + h1(key, m)) % m 

def HASH_INSERT(T, probing, key, m, h, hd = None):
	i = 0
	while True:
		j = linearProbing(key, i, m, h, hd)
		if T[j] == None:
			T[j] = key
			return j
		if i == m:
			return -1
		else:
			i = i + 1

def HASH_SEARCH(T, probing, key, m, h, hd = None):		
	i = 0
	while True:
		j = linearProbing(key, i, m, h, hd)
		if T[j] == key:
			return j
		if T[j] == None or i == m:
			return None
		i = i + 1

def test(n, m):
	global h
	hash_table = []
	numbers = random.sample(range(1, n+1), n)
	for i in range(0, m):
		hash_table.append([None])

	# (i)
	start = time.clock()
	for num in numbers:
		if HASH_INSERT(hash_table, linearProbing, num, m, firstHashFunc) == -1:
			print("hash table overflow")
			return
	endInsert = time.clock() - start
	# (ii)
	randomInx = random.choice(numbers)
	start = time.clock()
	indx = HASH_SEARCH(hash_table, linearProbing, num, m, firstHashFunc, secondHashFunc)
	endSearch = time.clock() - start 
	print("n = " + str(n) + "|m = " + str(m) + "|timeInserting = " + str(endInsert) + "|timeSearching = " + str(timeSearching))


if __name__ == "__main__":
	for n in [10000, 50000, 100000]:
			for m in [n, n//2, n//4]:
				test(n, m)