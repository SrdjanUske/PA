import time
import random
import math

def counting_sort(A, B, k):
    C = []

    for i in range(0, k + 1):
        B.append(0)    

    for i in range(0, k + 1):
        C.append(0)

    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1

    for i in range(1, k + 1):
        C[i] = C[i] + C[i - 1]

    for j in range(len(A) - 1, -1, -1):
       # print("A[" + str(j) + "] = " + str(A[j]))
       # print("C[A[" + str(j) + "]] = " + str(C[A[j]]))
       # print("B[C[A[" + str(j) + "]]] = " + str(B[C[A[j]]]))
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]] - 1

A = [6, 5, 5, 3, 8, 7, 4, 2, 1, 9]

# [0, 0, 1, 3, 3, 4, 7, 7, 9, 9]
# [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

B = []
C = random.sample(range(0, 5000), 3000)
D = []

for i in range(0, len(C)):
    C[i] = math.floor(C[i] / 100)

start = time.clock()
counting_sort(A, B, max(A))
end = time.clock()
print("Vreme izvrsavanja za n = 10: ", (end - start)*1000)
print(B)

start = time.clock()
counting_sort(C, D, 50)
end = time.clock()
print("Vreme izvrsavanja za n = 5000: ", (end - start)*1000)