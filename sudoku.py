import random
from numpy import transpose


"""
Sudoku

O Sudoku é um jogo simples, onde há um tabuleiro 9 x 9 cujo objetivo é preenchê-lo completamente de acordo com algumas regras:
0 - board 9 x 9  --  check
1 - Apenas números de 1 a 9  --  check
2 - Não é permitido números repetidos na mesma linha
3 - Não é permitido números repetidos na mesma coluna
4 - Não é permitido o mesmo número em um quadrante de 3 x 3
"""

class Sudoku:

    def __init__(self) -> None:
        self.digits = [int(i) for i in range(1, 10)]
        self.board = [[i for i in range(9)] for _ in range(9)]

    # validations
    def verify_row_repetition(self, e, choice, row):
        for i in row:
            while choice == i or choice in row:
                choice = random.choice(self.digits)
            return choice

    def fill_board(self):
        pass
# transposed_board = transpose(board)

# for i in transposed_board:
#     print(i)
if __name__ == '__main__':

    sudoku = Sudoku()
    board = sudoku.board
    digits = sudoku.digits
    #  main loop
    for i, r in enumerate(board):
        for e in r:
            r[e] = sudoku.chose_number()
        print(i, r)
