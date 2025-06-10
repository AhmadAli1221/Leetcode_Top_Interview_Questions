def rotate(matrix: list[list[int]]) -> None:
    rows = len(matrix)
    columns = len(matrix[0])

    res = []
    for each_row in range(columns):
        lst = []
        for rev_col in range(rows-1,-1,-1):
            lst.append(matrix[rev_col][each_row])
            rev_col -= 1
        res.append(lst)
    matrix.clear()
    matrix.extend(res)
