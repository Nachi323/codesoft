import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        
        self.create_board()
    
    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=" ", font=('Arial', 30),
                                                width=5, height=2,
                                                command=lambda row=i, col=j: self.handle_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)
    
    def handle_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner() or self.check_draw():
                self.end_game()
            else:
                self.switch_player()
                self.make_ai_move()
    
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def make_ai_move(self):
        best_score = float('-inf')
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        
        row, col = best_move
        self.board[row][col] = 'O'
        self.buttons[row][col].config(text='O')
    
    def minimax(self, board, depth, is_maximizing):
        winner = self.check_winner(board)
        if winner:
            if winner == 'X':  # Human player
                return -10 + depth
            elif winner == 'O':  # AI player
                return 10 - depth
            else:
                return 0  # Draw
        
        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'  # AI's move
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = ' '  # Undo move
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'  # Human's move
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = ' '  # Undo move
                        best_score = min(score, best_score)
            return best_score
    
    def check_winner(self, board=None):
        if board is None:
            board = self.board
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != ' ':
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != ' ':
                return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return board[0][2]
        return None
    
    def check_draw(self, board=None):
        if board is None:
            board = self.board
        for row in board:
            if ' ' in row:
                return False
        return True
    
