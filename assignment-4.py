board = [' '] * 9
WINS = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)]
 
def winner(p):
    return any(board[a] == board[b] == board[c] == p for a, b, c in WINS)
 
def show():
    for r in range(3):
        print(" " + " | ".join(board[r * 3:r * 3 + 3]))
    print()
 
def minimax(is_max):
    if winner('O'): return 1
    if winner('X'): return -1
    if ' ' not in board: return 0
 
    scores = []
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O' if is_max else 'X'
            scores.append(minimax(not is_max))
            board[i] = ' '
    return max(scores) if is_max else min(scores)
 
def best_move():
    best, move = -2, None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best:
                best, move = score, i
    return move
 
print("Positions are 1-9, left to right, top to bottom.")
while True:
    show()
    i = int(input("Your move (1-9): ")) - 1
    if not 0 <= i < 9 or board[i] != ' ':
        print("Invalid move, try again.")
        continue
    board[i] = 'X'
    if ' ' not in board: show(); print("Draw!"); break
 
    board[best_move()] = 'O'
    if winner('O'): show(); print("Computer wins!"); break
    if ' ' not in board: show(); print("Draw!"); break