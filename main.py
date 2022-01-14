from time import time, sleep
from solver import print_board, solve

board = [[0, 0, 0, 0, 0, 0, 8, 0, 2],
         [0, 0, 1, 0, 0, 9, 0, 0, 3],
         [0, 2, 0, 0, 8, 3, 0, 6, 0],
         [0, 0, 0, 7, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 9, 0, 0, 0, 0],
         [0, 7, 3, 0, 0, 0, 0, 4, 0],
         [0, 4, 0, 1, 0, 0, 6, 3, 0],
         [7, 8, 6, 0, 0, 0, 0, 0, 0],
         [0, 3, 0, 0, 0, 0, 0, 0, 7]
         ]

inp = input("Would you like to enter the board(y/n)? ").lower()
if inp == "n" or inp == "no":
    pass
elif inp == "y" or inp == "yes":
    print("Enter board rows one by one. Eg. Row 1: 1 0 0 2 3 5 0 2 0")
    board = []
    print()
    for i in range(9):
        row = input(f"Row {i+1}: ").split()
        l = [int(x) for x in row]
        board.append(l)


def main(board_to_solve):
    initial_time = time()
    print("Question:")
    print_board(board_to_solve)
    solve(board_to_solve)
    print()
    print("Solution:")
    print_board(board_to_solve)
    print()
    final_time = time()
    print(f'Time taken: {round(final_time - initial_time, 3)} s')

    from solver import steps
    print(f'Steps taken: {steps}')
    print()


main(board)
input("Press enter to exit...")
