def searchMatrix(matrix):
    for row in matrix:
        for col in row:
            if target == col:
                return True
    return False

