import random
from random import randint
import time

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
    temp = A[i + 1]
    A[i + 1] = A[r]
    A[r] = temp
    return i + 1

def randomized_partition(A, p, r):
    i = random.randint(p, r)
    temp = A[r]
    A[r] = A[i]
    A[i] = temp
    return partition(A, p, r)

def randomized_quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        randomized_quicksort(A, p, q - 1)
        randomized_quicksort(A, q + 1, r)

A = [54, 26, 93, 17, 77, 31, 44, 55, 20, 10]
B = random.sample(range(1, 50000), 5000)

start = time.clock()
randomized_quicksort(A, 0, len(A) - 1)
end = time.clock()
print("Vreme izvrsavanja za n = 10: ", (end - start)*1000)
print(A)

start = time.clock()
randomized_quicksort(B, 0, len(B) - 1)
end = time.clock()
print("Vreme izvrsavanja za n = 5000: ", (end - start)*1000)