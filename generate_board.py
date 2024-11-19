import random


def is_valid(board, row, col, num):
    """Verifica se o número pode ser colocado na posição (row, col)."""
    # Verifica a linha e a coluna
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Verifica a subgrade 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve_board(board):
    """Resolve o tabuleiro usando backtracking."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_board(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def generate_full_board():
    """Gera um tabuleiro de Sudoku completo."""
    board = [[0 for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                num_list = list(range(1, 10))
                random.shuffle(num_list)
                for num in num_list:
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_board(board):
                            return board
                        board[i][j] = 0
                return board
    return board


def remove_numbers(board, num_holes):
    """Remove números do tabuleiro completo para criar um desafio."""
    for _ in range(num_holes):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
    return board


def generate_sudoku(num_holes=40):
    """
    Gera um tabuleiro de Sudoku com um número especificado de espaços vazios.

    :param num_holes: Número de células vazias no tabuleiro.
    :return: Tabuleiro de Sudoku com espaços vazios.
    """
    full_board = generate_full_board()
    challenge_board = remove_numbers(full_board, num_holes)
    return challenge_board
