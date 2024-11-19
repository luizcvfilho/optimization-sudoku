
# Optimization-Sudoku

Este repositório implementa uma solução para o problema do Sudoku utilizando técnicas de otimização matemática, com foco em programação linear inteira (PLI). A abordagem é construída sobre a modelagem de restrições do Sudoku como um problema de satisfação de restrições e resolvida utilizando a biblioteca **PuLP** em Python.

## **Recursos**
- Modelagem do Sudoku como um problema de **programação linear inteira**.
- Suporte para resolver tabuleiros iniciais personalizados.
- Interface gráfica interativa para visualizar o tabuleiro e alternar entre o estado inicial e a solução.
- Geração de tabuleiros aleatórios com níveis de dificuldade ajustáveis.

## **Tecnologias Utilizadas**
- **Python**: Linguagem principal.
- **PuLP**: Para resolver o modelo de otimização.
- **Tkinter**: Para a interface gráfica.

## **Como Usar**
1. Clone o repositório:
   ```bash
   git clone https://github.com/luizcvfilho/optimization-sudoku.git
   cd optimization-sudoku
   ```
2. Instale as dependências:
   ```bash
   pip install pulp
   ```
3. Execute o programa:
   ```bash
   python main.py
   ```
4. Utilize a interface gráfica para:
   - Gerar novos tabuleiros.
   - Resolver tabuleiros personalizados.
   - Alternar entre o estado inicial e a solução.

## **Exemplo de Uso**
### **Tabuleiro Inicial**
```plaintext
[9, 1, 0, 0, 0, 0, 6, 0, 8]
[3, 0, 0, 6, 7, 8, 1, 2, 0]
[6, 0, 8, 1, 2, 0, 3, 4, 0]
[0, 0, 3, 0, 5, 6, 8, 0, 7]
[0, 0, 6, 8, 0, 0, 0, 0, 3]
[7, 8, 0, 0, 1, 0, 4, 5, 0]
[0, 0, 7, 0, 0, 0, 9, 0, 4]
[5, 6, 0, 9, 0, 4, 7, 3, 0]
[8, 9, 0, 0, 0, 0, 5, 0, 0]
```

### **Tabuleiro Resolvido**
```plaintext
[9, 1, 5, 3, 4, 2, 6, 7, 8]
[3, 4, 2, 6, 7, 8, 1, 2, 9]
[6, 7, 8, 1, 2, 5, 3, 4, 9]
[1, 2, 3, 4, 5, 6, 8, 9, 7]
[4, 5, 6, 8, 9, 7, 2, 1, 3]
[7, 8, 9, 2, 1, 3, 4, 5, 6]
[2, 3, 7, 5, 6, 1, 9, 8, 4]
[5, 6, 4, 9, 8, 4, 7, 3, 1]
[8, 9, 1, 7, 3, 2, 5, 6, 2]
```
