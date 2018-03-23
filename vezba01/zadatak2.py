import sys

DEFAULT_NUM = 5

def square_sum(N):
	if N == 1:
		return 1
	else:
		return N**2 + square_sum(N - 1)
		

if len(sys.argv) > 1:
	N = int(sys.argv[1])

else:
	N = DEFAULT_NUM

print("Suma kvadrata prvih " + str(N) + " brojeva iznosi: " + str(square_sum(N)))