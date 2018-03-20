import random
import time
import sys

def insertion(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

def buble(A):
    for i in range(0, len(A) - 1):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp

def linear(A, element):
    for i in range(0, len(A)):
        if A[i] == element:
            return i
    return -1

def binary(A, element):
    mid = int((len(A)) / 2)
    if len(A) == 0:
        sys.exit(0)
    if element == A[mid]:
        return mid
    elif element > A[mid]:
        return mid + binary(A[mid:], element)
    elif element < A[mid]:
        return binary(A[:mid], element)
    else:
        sys.exit(0)

def random_list (min, max, elements):
    list = random.sample(range(min, max), elements)
    return list

l = random_list(1, 50000, 3000)
m = l
n = m

start_time = time.clock()

insertion(l)

end_time = time.clock() - start_time
print("Insertion duration: ", end_time)

start_time = time.clock()

buble(m)

end_time = time.clock() - start_time
print("Buble duration: ", end_time)

n[255] = 77

start_time = time.clock()

itemL = linear(n, 77)

end_time = time.clock() - start_time
print("Linear duration: ", end_time)


start_time = time.clock()

itemB = binary(l, l[679])

end_time = time.clock() - start_time
print("Binary duration: ", end_time)




