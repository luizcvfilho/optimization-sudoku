import tkinter as tk
from tkinter import messagebox
from generate_board import generate_sudoku
from sudoku_solver import solve_sudoku


# Verifica se o valor inserido está correto com base na solução
def update_color_solution(event, solution):
    entry = event.widget
    row, col = entry.grid_info()["row"], entry.grid_info()["column"]
    value = entry.get()

    if value.isdigit():
        num = int(value)
        if num == solution[row][col]:
            entry.config(fg="black")  # Número correto
        else:
            entry.config(fg="red")  # Número incorreto
    else:
        entry.config(fg="red")


# Exibe um tabuleiro na interface
def display_board(board, cells, solution=None):
    clear_board(cells)
    for i in range(9):
        for j in range(9):
            value = board[i][j]
            cells[i][j].delete(0, tk.END)  # Limpa a célula
            if value != 0:
                cells[i][j].insert(0, str(value))  # Insere o valor
                cells[i][j].config(state="disabled", fg="black")  # Número fixo
            else:
                cells[i][j].config(state="normal", fg="black")  # Célula editável
                if solution:
                    # Adicionar evento para verificar se está correto
                    cells[i][j].bind(
                        "<KeyRelease>",
                        lambda event, s=solution: update_color_solution(event, s),
                    )


# Obtem o tabuleiro atual da interface
def get_board_from_ui(cells):
    return [
        [
            0 if not cells[i][j].get().isdigit() else int(cells[i][j].get())
            for j in range(9)
        ]
        for i in range(9)
    ]


# Resolve o Sudoku e exibe o resultado
def solve_and_display(board, cells):
    solved_board = solve_sudoku(board)
    if isinstance(solved_board, str):
        messagebox.showerror("Erro", solved_board)
    else:
        display_board(solved_board, cells)


# Gera um novo tabuleiro
def generate_and_display(cells):
    # Gera o tabuleiro inicial
    board = generate_sudoku(num_holes=40)
    print("Tabuleiro Inicial\n")
    for row in board:
        print(row)
    # Calcula a solução para o tabuleiro
    solved_board = solve_sudoku(board)
    print("\n\nTabuleiro Resolvido\n")
    for row in solved_board:
        print(row)

    # Exibe o tabuleiro inicial e configura validação baseada na solução
    display_board(board, cells, solution=solved_board)


def clear_board(cells):
    """
    Limpa todas as células do tabuleiro na interface.
    """
    for i in range(9):
        for j in range(9):
            cells[i][j].delete(0, tk.END)
            cells[i][j].config(state="normal", fg="black")  # Redefine como editável


# Interface principal
def create_gui():
    root = tk.Tk()
    root.title("Sudoku Solver")
    root.geometry("400x500")

    # Grid de células
    cells = [[None for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            # Configurar bordas espessas entre subgrades 3x3
            border_top = 2 if i % 3 == 0 else 1
            border_left = 2 if j % 3 == 0 else 1
            border_bottom = 2 if i == 8 else 1
            border_right = 2 if j == 8 else 1

            entry = tk.Entry(
                root,
                width=2,
                font=("Arial", 18),
                justify="center",
                highlightthickness=1,
                bd=0,
                relief="solid",
                highlightbackground="black",
                highlightcolor="black",
            )
            entry.grid(
                row=i,
                column=j,
                padx=(border_left, 0),
                pady=(border_top, 0),
                ipadx=5,
                ipady=5,
            )
            cells[i][j] = entry

    # Botão para resolver
    solve_button = tk.Button(
        root,
        text="Resolver Sudoku",
        font=("Arial", 14),
        command=lambda: solve_and_display(get_board_from_ui(cells), cells),
    )
    solve_button.grid(row=10, column=0, columnspan=4, pady=10)

    # Botão para gerar
    generate_button = tk.Button(
        root,
        text="Gerar Sudoku",
        font=("Arial", 14),
        command=lambda: generate_and_display(cells),
    )
    generate_button.grid(row=10, column=5, columnspan=4, pady=10)

    # Rodar a interface
    root.mainloop()
