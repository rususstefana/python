board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

def draw_board():
    
    print('\n' * 50)

    print('    A   B   C  ')
    print('  +---+---+---+')

    for i in range(3):
        print(i+1, '| ', end = '')
        
        for j in range(3):
            print(board[i][j], '| ', end='')
        print()

        print('  +',end ='')
        for j in range(3):
            print('---+', end='')
        print()

    print('    A   B   C  ')

def extract_cell(opt):
    # TODO implement
    return (0, 0)

def cell_empty(cell):
    # TODO implement
    return False

def cell_exists(cell):
    # TODO implement
    return False

def find_winner():
    # TODO implement
    return None

while True:
    # draw board
    draw_board()
    
    # read user option
    option = input(' Cell (ex: A2, B3, C1; Q to quit): ')
    # Q means exit
    if option.lower() == 'q':
        exit()

    # extract coordiates from option to cell concept
    cell = extract_cell(option)

    # verify if cell exists
    if not cell_exists(cell):
        print('Cell does not exist')
        input('Press enter')
        continue

    # verify if cell is free
    if not cell_empty(cell):
        print('Cell is already marked')
        input('Press enter')
        continue

    # draw board with selected cell
    draw_board()

    # verify if user won
    winner = find_winner()

    # if won, exit
    if winner == 'X':
        print("X won")
        break
    # if not won, give enter to give the computer option to win

    # if there are no moves left end with a draw

    # artificial inteligence

    # check if computer won

    # if computer won, exit game

    # if there are no moves left end with a draw
    