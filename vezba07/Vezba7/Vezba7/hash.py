import sys
import math
import random
import time


p = 23
m = 100
a = random.randint(1, p)
b = random.randint(0, p)

class Data:
    def __init__(self, key = None, literal = None):
        self.key = key
        self.literal = literal
    def getKey(self):
        return self.key
    def printData(self):
        print(str(self.key) + " " + str(self.literal))

def some_method(k):
    global m
    mm = random.randint(-math.inf, m)
    return 1 + (k % mm)

def division_method(k):
    global m
    return k % m    

def multiplication_method(k):
    global m
    A = (math.sqrt(5) - 1) / 2
    return math.floor(m * ((k*A) % 1))

def universal_hashing(k):
    global m, p, a, b
    return ((a*k + b) % p) % m

def chain_hash_search(T, k, function_name):

    position = function_name(k)
   
    for i in range(0, len(T[position])):
        if T[position][i].key == k:
            return T[position][i]
    return None

def chainned_hash_delete(T, x, function_name):
    
    position = function_name(x.key)    

    for i in range(0, len(T[position])):
        if T[position][i].key == x.key:
            del T[position][i]

def chained_cash_insert(T, x, function_name):

    position = function_name(x.key)
    
    if chain_hash_search(T, x.key, function_name) != None: 
        chainned_hash_delete(T, x, function_name)
    T[position].append(x)

def linear(function_name, k, i):
    global m
    return (function_name(k) + i) % m

def qudratic(function_name, k, c1, c2):
    global m
    return (function_name(k) + c1*i + c2*i*i) % m
    
def double_hashing(function_name1, function_name2, k):
    global m
    return (function_name1(k) + function_name2(k)) % m

def hash_insert(T, k, function_name, function_surname):
    global m    
    i = 0
    while not(i == m):
        j = function_name(function_surname, k, i)
        if T[j] == None:
            T[j] = k
            return j
        else:
            i = i + 1
    print("hash table error") 

def hash_search(T, k, function_name, function_surname):
    global m    
    i = 0
    j = function_name(T, k, i)
    if T[j] == None:
        T[j] = k
        return j
    else:
        i = i + 1

    while not(i == m and T[j] == None):
        j = function_name(function_surname, k, i)
        if T[j] == None:
            T[j] = k
            return j
        else:
            i = i + 1

    return None


#d = multiplication_method(250)
#d = division_method(250)
#d = universal_hashing(250)
#print(d)

T = [list() for i in range(0, m)]
elements = []

for i in range(0, 10000):
    elements.append(Data(random.randint(0, p - 1), i + 1))

for i in range(0, 10000):
    chained_cash_insert(T, elements[i], universal_hashing)

position = random.randint(0, 10000)
data = chain_hash_search(T, elements[position].key, universal_hashing)
data.printData()

chainned_hash_delete(T, elements[position], universal_hashing)
data = chain_hash_search(T, elements[position].key, universal_hashing)
print(data)

t = time.clock()
data = chain_hash_search(T, elements[position].key, universal_hashing)
t1 = time.clock() - t
print(t1)

t = time.clock()
data = chain_hash_search(T, elements[position].key, multiplication_method)
t1 = time.clock() - t
print(t1)

c1 = 1 / 2
c2 = 1 / 2

TT = [list() for i in range(0, m)]
Eelements = []

for i in range(0, 10000):
    Eelements.append(Data(random.randint(0, p - 1), i + 1))

for i in range(0, 10000):
    hash_insert(TT, Eelements[i].key, linear, universal_hashing)
