# Write a function that receives as parameter a matrix and will return the matrix obtained by replacing
# all the elements under the main diagonal with 0 (zero).

def printmatrix(mat, n, m):
    for i in range(n):
        for j in range(m):
            print(mat[i][j], end=" ")

        print()


# function to change the values
# of elements under main diag to 0
def makelemzero(mat, n, m):
    for i in range(n):
        for j in range(m):
            if (i > j):
                mat[i][j] = 0

    printmatrix(mat, n, m)



n = 3
m = 3
mat = [ [2, 1, 7],
        [3, 7, 2],
        [5, 4, 9] ]

makelemzero(mat, n, m)