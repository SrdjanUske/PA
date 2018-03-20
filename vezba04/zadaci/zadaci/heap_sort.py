import time
import random
import math

def parent(i):
    return i / 2

def left(i):
    return 2*i

def right(i):
    return 2*i + 1

def max_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)
    largest = 0
    
    if (l <= heap_size and A[l] > A[i]):
        largest = l
    else:
        largest = i

    if (r <= heap_size and A[r] > A[largest]):
        largest = r

    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        max_heapify(A, largest, heap_size)

def build_max_heap(A):
    heap_size = len(A) - 1
    
    for i in range(math.floor(len(A)/2), -1, -1):
        max_heapify(A, i, heap_size)

    return heap_size

def heapsort(A):
    
    heap_size = build_max_heap(A)
    
    for i in range(len(A)-1, 0, -1):
        temp = A[i]
        A[i] = A[0]
        A[0] = temp
        heap_size = heap_size - 1
        max_heapify(A, 0, heap_size)

A = [16, 9, 10, 3, 8, 7, 4, 2, 1, 5]
B = random.sample(range(1, 50000), 5000)

start = time.clock()
heapsort(A)
end = time.clock()
print("Vreme izvrsavanja za n = 10: ", (end - start)*1000)
print(A)

start = time.clock()
heapsort(B)
end = time.clock()
print("Vreme izvrsavanja za n = 5000: ", (end - start)*1000)