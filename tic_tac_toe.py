def print_board(board):
    """Print the board."""
    print('---------')
    for row in board:
        print(f'| {row[0]} {row[1]} {row[2]} |')
    print('---------')


def symbol_won(board, symbol):
    """Check if a symbol has 3 in a row."""
    for row in board:
        if row == [symbol] * 3:
            return True
    for col_id in range(3):
        col = ''.join(board[x][col_id] for x in range(3))
        if col == symbol * 3:
            return True
    diagonal = ''.join(board[x][x] for x in range(3))
    if diagonal == symbol * 3:
        return True
    diagonal = ''.join(board[x][2-x] for x in range(3))
    if diagonal == symbol * 3:
        return True
    return False


def analyse_board(board):
    """Figure out what the state of the board is."""
    count_empty = [cell for row in board for cell in row].count('_')

    if symbol_won(board, 'X'):
        return 'X wins'
    if symbol_won(board, 'O'):
        return 'O wins'
    if count_empty == 0:
        return 'Draw'
    return 'Game not finished'


def translate_coordinates(i):
    """Turn the coordinates from the game to list indexes."""
    return 3 - i[1], i[0] - 1


def validate_coordinates(i, board):
    """Check if the user inserted valid coordinates."""
    try:
        i = list(map(int, i))
    except ValueError:
        print('You should enter numbers!')
        return False
    if i[0] not in range(1, 4) or i[1] not in range(1, 4):
        print('Coordinates should be from 1 to 3!')
        return False
    x, y = translate_coordinates(i)
    if board[x][y] != '_':
        print('This cell is occupied! Choose another one!')
        return False
    return True


def make_move(board, symbol):
    """Ask the user for their coordinates."""
    while True:
        i = input('Enter the coordinates: >').split()
        if validate_coordinates(i, board):
            i = list(map(int, i))
            x, y = translate_coordinates(i)
            board[x][y] = symbol
            print_board(board)
            break


def play_game():
    """Start the game."""
    board = [['_'] * 3 for _ in range(3)]
    turn = 'X'
    while True:
        print_board(board)
        make_move(board, turn)
        state = analyse_board(board)
        if state != 'Game not finished':
            print(state)
            break
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


play_game()
