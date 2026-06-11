def spiralmatrix(matrix):
    res = []
    print(matrix)

    while matrix:
        res += matrix.pop(0)
        print(res)
        if matrix and matrix[0]:
            for row in matrix:
                res.append(row.pop())

            if matrix:
                res += matrix.pop()[::-1]
                print(matrix)
            for row in reversed(matrix):
                if row:
                    res.append(row.pop(0))


    return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralmatrix(matrix))
