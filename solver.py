steps = 0


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i!= 0:
            print("- - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(bo[i][j] if bo[i][j] != 0 else " ")
            else:
                print(str(bo[i][j]) if bo[i][j] != 0 else " ", end="")
                print(" ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, col
    return False


def valid(bo, num, pos):
    # Row wise
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Column wise
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Block wise
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def solve(bo):
    global steps
    find = find_empty(bo)
    if not find:
        # print(steps)
        return True
    else:
        row, col = find
    steps += 1
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                # print(steps)
                return True
            bo[row][col] = 0
    return False
