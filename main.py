from time import time, sleep
from solver import print_board, solve

board = [[7, 3, 2, 0, 5, 4, 8, 0, 1],
          [6, 0, 8, 0, 2, 0, 0, 4, 0],
          [1, 0, 4, 0, 8, 0, 6, 0, 2],
          [0, 0, 0, 9, 0, 0, 0, 1, 3],
          [9, 2, 0, 8, 1, 0, 0, 0, 0],
          [3, 1, 0, 4, 0, 0, 9, 0, 0],
          [0, 4, 0, 0, 0, 0, 2, 0, 0],
          [2, 0, 3, 1, 0, 0, 0, 0, 0],
          [5, 0, 0, 0, 3, 0, 0, 6, 0]
          ]


def main(board_to_solve):
    initial_time = time()
    print("Question:")
    print_board(board_to_solve)
    solve(board_to_solve)
    print("")
    print("Solution:")
    print_board(board_to_solve)
    print("")
    final_time = time()
    print(f'Time taken: {round(final_time - initial_time, 3)} s')

    from solver import steps
    print(f'Steps taken: {steps}')
    print('')
    sleep(10)


main(board)
