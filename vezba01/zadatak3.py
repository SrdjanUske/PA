import sys

N = len(sys.argv)

if N == 1:

	string1 = "srdjan"
	string2 = "usorac"

elif N == 2:

	string1 = sys.argv[1]
	string2 = "usorac"

elif N == 3:

	string1 = sys.argv[1]
	string2 = sys.argv[2]

combine = 2 * string1[0:3] + string2[len(string2) - 3:]
print("Combination: " + combine)