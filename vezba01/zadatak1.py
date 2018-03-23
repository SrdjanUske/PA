import sys

DEFAULT_NUM = 5

def sum(N):
	if N == 1:
		return 1
	else:
		return N + sum(N - 1)


if len(sys.argv) > 1:
	N = int(sys.argv[1])

else:
	N = DEFAULT_NUM

print("Suma prvih " + str(N) + " brojeva iznosi: " + str(sum(N)))
