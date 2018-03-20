import time
import random
import math

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

def bucket_sort(A):
    
    B = []

    for i in range(0, n):
        B.append([])

    for i in range(0, len(A)):
        B[math.floor(A[i] / 10)].append(A[i])

    for i in range(0, n):
        insertionSort(B[i])

    C = []
    for i in range(0, n):
        C = C + B[i]

    return C
    

n = 10    
       
A = [99, 88, 77, 66, 55, 44, 33, 22, 11, 1, 0, 10, 21, 32, 43, 54, 65, 76, 87, 98, 56, 65, 32, 78, 90, 13, 53, 43]
B = random.sample(range(0, 5000), 2000)

for i in range(0, len(B)):
    B[i] = math.floor(B[i] / 50)

start = time.clock()
A = bucket_sort(A)
end = time.clock()
print("Vreme izvrsavanja za n = 28: ", (end - start)*1000)
print(A)

start = time.clock()
bucket_sort(B)
end = time.clock()
print("Vreme izvrsavanja za n = 2000: ", (end - start)*1000)