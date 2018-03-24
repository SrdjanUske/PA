import math
import sys
import random

heap_size = 0

def parent(i):
    return math.floor(i / 2)

def left(i):
    return 2*i + 1

def right(i):
    return 2*(i + 1)

def heap_maximum(A):
    return A[0]

def heap_increase_key(A, i, key):
    if key < A[i]:
        print("new key is smaller than current key")
        return

    A[i] = key
    
    while i > 0 and A[parent(i)] < A[i]:
        temp = A[parent(i)]
        A[parent(i)] = A[i]
        A[i] = temp
        i = parent(i)

def max_heap_insert(A, key):
    global heap_size
    
    heap_size += 1
    A.append(-math.inf)

    heap_increase_key(A, heap_size - 1, key)

def max_heapify(A, i):
    global heap_size    

    l = left(i)
    r = right(i)
    
    if l <= heap_size - 1 and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r <= heap_size - 1 and A[r] > A[largest]:
        largest = r

    if not(largest == i):
        temp = A[largest]
        A[largest] = A[i]
        A[i] = temp
        max_heapify(A, largest)

def heap_extract_max(A):
    global heap_size

    if heap_size < 1:
         print("heap underflow")
         return
    
    max = A[0]
    A[0] = A[heap_size - 1]
    heap_size -= 1
    max_heapify(A, 0)
    return max

if __name__ == "__main__":
    N = 20
    lista = random.sample(range(0, 2*N), N)
    red = []
    print("Ulazni red: " + str(lista) + "\n")
    sortirtan_red = []

    # (i)
    for i in range(0, N):
        max_heap_insert(red, lista[i])

    print("Binarno stablo: " + str(red) + "\n")

    # (ii)
    for i in range(0, N):
        sortirtan_red.append(heap_extract_max(red))

    print("Sortiran red: " + str(sortirtan_red) + "\n")
    