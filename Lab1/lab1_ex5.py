# 5.Given a square matrix of characters write a script that prints
# the string obtained by going through the matrix in spiral order
# (as in the example):
# firs      1  2  3  4    =>   first_python_lab
# n_lt      12 13 14 5
# oba_      11 16 15 6
# htyp      10 9  8  7

def matrixinspiralorder(a):
    m = len(a)
    n = len(a[0])
    k = 0
    l = 0

    while (k < m and l < n):

        for i in range(l, n):
            print(a[k][i], end="")

        k += 1

        for i in range(k, m):
            print(a[i][n - 1], end="")

        n -= 1

        if (k < m):

            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end="")

            m -= 1

        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end="")

            l += 1

x = ["firs", "n_lt", "oba_", "htyp"]

print("Result for given example is:")
matrixinspiralorder(x)