def sudoku_check(board: list[list]):
    for i in range(9):
#rows
        lst = []
        for rows in range(9):
            if board[i][rows] == '.':
                continue
            elif board[i][rows] not in lst:
                lst.append(board[i][rows])
            else:
                return False
#column
        lst = []
        for column in range(9):
            if board[column][i] == '.':
                continue
            elif board[column][i] not in lst:
                lst.append(board[column][i])
            else:
                return False
#box
    for box_row in [0,3,6]:
        for box_col in [0,3,6]:
            lst = []
            for x in range(3):
                for y in range(3):
                    if board[box_row + x][box_col + y] == '.':
                        continue
                    elif board[box_row + x][box_col + y] not in lst:
                        lst.append(board[box_row + x][box_col + y])
                    else:
                        return False
    return True