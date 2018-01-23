def minesweeper(matrix):

    row = len(matrix)
    col = len(matrix[0])

    for i in range(len(row) - 1):
        for j in range(len(col) - 1):

            if i == 0:
