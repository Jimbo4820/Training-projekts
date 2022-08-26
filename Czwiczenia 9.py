from random import randrange
board = [[1,2,3],[4,5,6],[7,8,9]]

def display_board(board):
    print(board[0])
    print(board[1])
    print(board[2])
#
# Funkcja, która przyjmuje jeden parametr zawierający bieżący stan tablicy
# i wyświetla go w oknie konsoli.
#

def enter_move(board):
    ruch = int(input("Wykonaj swój ruch"))
    if i in board:
        board.insert(ruch, "o")
    else:
        enter_move(board)
#
# Funkcja, która przyjmuje parametr odzwierciedlający biężący stan tablicy,
# prosi użytkownika o wykonanie ruchu, 
# sprawdza dane wejściowe i aktualizuje tablicę zgodnie z decyzją użytkownika.
#

#def make_list_of_free_fields(board):
#
# Funkcja, która przegląda tablicę i tworzy listę wszystkich wolnych pól; 
# lista składa się z krotek, a każda krotka zawiera parę liczb odzwierciedlających rząd i kolumnę.
#

#def victory_for(board, sign):
#
# Funkcja, która dokonuje analizy stanu tablicy w celu sprawdzenia
# czy użytkownik/gracz stosujący "O" lub "X" wygrał rozgrywkę.
#

def draw_move(board):
    if board[1][1] == 5 :
        board[1][1] = "x"
    for i in range(10): print(randrange(8))

#
# Funkcja, która wykonuje ruch za komputer i aktualizuje tablicę.
#
draw_move(board)
display_board(board)
enter_move(board)