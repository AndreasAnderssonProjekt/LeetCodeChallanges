def setZeros(matrix):
    col0 = 1
    row0 = 1

    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

                if i == 0:
                    row0 = 0

                if j == 0:
                    col0 = 0

    for i in range(1,m):
        if matrix[i][0] == 0:
            for j in range(n):
                matrix[i][j] = 0

    for j in range(1,n):
        if matrix[0][j] == 0:
            for i in range(m):
                matrix[i][j] = 0

    if col0 == 0:
        for i in range(m):
            matrix[i][0] = 0

    if row0 == 0:
        for j in range(n):
            matrix[0][j] = 0

    return matrix
