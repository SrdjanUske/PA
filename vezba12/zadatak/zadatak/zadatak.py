import time

def LCS(S, n, T, m):
    if n < 0 or m < 0:
        return 0
    if S[n] == T[m]: 
        return 1 + LCS(S, n - 1, T, m - 1)
    else:
        return max(LCS(S, n - 1, T, m), LCS(S, n, T, m - 1))

def LCS_LENGTH(X, Y):
    m = len(X)
    n = len(Y)
    b = []
    c = []
    for i in range(0, m + 1):
        c.append([])
        for j in range(0, n + 1):
             c[i].append(0)
    for i in range(0, m):
        b.append([])
        for j in range(0, n):
             b[i].append(0)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i-1][j-1] = '\\'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i-1][j-1] = '|'
            else:
                c[i][j] = c[i][j-1]
                b[i-1][j-1] = '-'
    return [c, b]

def PRINT_LCS(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j-1] == '\\':
        PRINT_LCS(b, X, i-1, j-1)
        print(X[i])
    elif b[i][j-1] == '|':
        PRINT_LCS(b, X, i-1, j)
    else:
        PRINT_LCS(b, X, i, j-1)

if __name__ == "__main__":
    print("Zadatak 1")
    print("---------")
    S = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
    n = len(S) - 1
    T = ['B', 'D', 'C', 'A', 'B', 'A']
    m = len(T) - 1
    start_time = time.clock()
    length = LCS(S, n, T, m)
    end_time = time.clock() - start_time
    print(length)
    print("\n" + "t = " + str(end_time) + "\n")

    print("Zadatak 2")
    print("---------")
    start_time = time.clock()
    [c, b] = LCS_LENGTH(S, T)
    end_time = time.clock() - start_time
    print(c)
    print(b)
    print("\n" + "t = " + str(end_time) + "\n")

    print("Zadatak 3")
    print("---------")
    PRINT_LCS(b, S, m, n)
    