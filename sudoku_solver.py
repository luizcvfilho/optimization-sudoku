from pulp import (
    LpProblem,
    LpVariable,
    LpMinimize,
    lpSum,
    LpBinary,
    LpStatus,
    PULP_CBC_CMD,
)


def solve_sudoku(board):
    """
    Resolve um Sudoku 9x9 usando programação linear inteira.

    :param board: Lista de listas representando o tabuleiro inicial.
                Use 0 para células vazias.
    :return: Tabuleiro resolvido ou mensagem de erro.
    """
    # Criação do problema
    problem = LpProblem("Sudoku_Solver", LpMinimize)

    # Variáveis de decisão: x[i][j][k] = 1 se o número k está na célula (i, j)
    x = [
        [
            [LpVariable(f"x_{i}_{j}_{k}", cat=LpBinary) for k in range(1, 10)]
            for j in range(9)
        ]
        for i in range(9)
    ]

    # Restrição 1: Cada célula contém exatamente um número
    for i in range(9):
        for j in range(9):
            problem += lpSum(x[i][j][k] for k in range(9)) == 1

    # Restrição 2: Cada número aparece exatamente uma vez em cada linha
    for i in range(9):
        for k in range(9):
            problem += lpSum(x[i][j][k] for j in range(9)) == 1

    # Restrição 3: Cada número aparece exatamente uma vez em cada coluna
    for j in range(9):
        for k in range(9):
            problem += lpSum(x[i][j][k] for i in range(9)) == 1

    # Restrição 4: Cada número aparece exatamente uma vez em cada subgrade 3x3
    for box_row in range(3):
        for box_col in range(3):
            for k in range(9):
                problem += (
                    lpSum(
                        x[i][j][k]
                        for i in range(box_row * 3, (box_row + 1) * 3)
                        for j in range(box_col * 3, (box_col + 1) * 3)
                    )
                    == 1
                )

    # Restrição 5: Respeitar os valores iniciais do tabuleiro
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                problem += x[i][j][board[i][j] - 1] == 1

    # Função objetivo (só precisamos de viabilidade, então é 0)
    problem += 0

    # Resolver o problema
    status = problem.solve(PULP_CBC_CMD(msg=False))

    # Interpretar a solução
    if LpStatus[status] == "Optimal":
        solved_board = [[0 for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                for k in range(9):
                    if x[i][j][k].value() == 1:
                        solved_board[i][j] = k + 1
        return solved_board
    else:
        return "Nenhuma solução encontrada."
