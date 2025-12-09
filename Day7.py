file = open("./Day7input")
board = file.read().split("\n")

def part_one(da_board):
    start_pos = (0,0)
  
    board = []
    for row in da_board:
        board.append(list(row))

    for i, elem in enumerate(board[0]):
        if elem == 'S':
            start_pos = (i,0)
            break

    return fall(start_pos[0], start_pos[1], board)

def part_two(da_board):
    start_pos = (0,0)
  
    board = []
    for row in da_board:
        board.append(list(row))

    count_board = make_count_board(board)

    for i, elem in enumerate(board[0]):
        if elem == 'S':
            start_pos = (i,1)
            break

    print_board(count_board)

    result_board = process_count_board(start_pos,count_board)

    
    print_board(result_board)

    print(result_board[-1])

    total = 0
    for elem in result_board[-1]:
        total += elem

    return total


    
    

def make_count_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
                board[i][j] = 0

    return board

def fall(x,y,board):
     board[y][x] = '|'
     next_tile_pos = (x,y+1)
     next_tile = get_tile(next_tile_pos[0],next_tile_pos[1], board)
     #print_board(board)

     if next_tile == 'Y':
          return 0
     elif next_tile == '.':
          return  fall(next_tile_pos[0], next_tile_pos[1], board)
     elif next_tile == '^':
          count1 = 0
          count2 = 0
          if get_tile(next_tile_pos[0] - 1, next_tile_pos[1], board) != 'X':
              count1 = fall(next_tile_pos[0] - 1, next_tile_pos[1], board)
          if get_tile(next_tile_pos[0] + 1, next_tile_pos[1], board) != 'X' and get_tile(next_tile_pos[0] + 2, next_tile_pos[1] - 1, board) != '^':
              count2 = fall(next_tile_pos[0] + 1, next_tile_pos[1], board)
          return 1 + count1 + count2
     else: 
        return 0
     
def quantum_fall(x,y,board):
    board[y][x] += 1 
    next_tile_pos = (x,y+1)
    next_tile = get_tile(next_tile_pos[0],next_tile_pos[1], board)
    #print_board(board)

    if next_tile == 'Y':
          return 1
    elif next_tile == '.' or next_tile == '|':
          return  quantum_fall(next_tile_pos[0], next_tile_pos[1], board)
    elif next_tile == '^':
          count1 = 0
          count2 = 0
          if get_tile(next_tile_pos[0] - 1, next_tile_pos[1], board) != 'X':
              count1 = quantum_fall(next_tile_pos[0] - 1, next_tile_pos[1], board)
          if get_tile(next_tile_pos[0] + 1, next_tile_pos[1], board) != 'X':
              count2 = quantum_fall(next_tile_pos[0] + 1, next_tile_pos[1], board)
          return count1 + count2
    else: 
        return 0
    
def process_count_board(start_pos, count_board):
    x = start_pos[0]
    y = start_pos[1]

    count_board[y][x] = 1

    board_height = len(count_board)
    board_width = len(count_board[0])

    print(board_width)

    for i in range(board_height - 1):
        for j in range(board_width):
            if type(count_board[i][j]) == int and count_board[i][j] > 0:
                match count_board[i+1][j]:
                    case '^':
                        if j > 0:
                            count_board[i+1][j-1] += count_board[i][j]
                        if j < board_width - 1:
                            count_board[i+1][j+1] += count_board[i][j]
                    case _:
                        count_board[i+1][j] += count_board[i][j]
                        

    return count_board

                    


def print_board(board):
    print("------------------------------------------")
    for row in board:
        line = ""
        for elem in row:
          line += str(elem) + ""
        print(line)
          
    print("------------------------------------------")

def clean_board(board):
    clean_board = []
    for row in board:
        clean_board.append(list(row))

    return clean_board

def get_tile(x,y,board):
     if y >= len(board):
          return 'Y'
     if x >= len(board[0]) or x < 0:
          return 'X'
     return board[y][x]
     

print(part_two(board))