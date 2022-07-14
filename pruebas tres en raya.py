

board = [[1 + i for i in range(3)]for i in range(3)]

for i in range(0,3):
    j = 4
    a = 7
    board[1][i] = i + j
    board[2][i] = i + a
    j -= 1
    a -= 1


def DisplayBoard(board=board):
    print(board[0],board[1],board[2], sep="\n")

def EnterMove(board=board):
    move = int(input("Ingresa tu movimiento, humano "))
    
    def validacion_de_ocupacion(fila, columna):
        if board[fila][columna] == "O" or board[fila][columna] == "X":
            print("Este casillero esta ocupado, ingresa otro humano")
            return EnterMove()
            
    if move == 1 or move == 2 or move == 3:
            validacion_de_ocupacion(0,(move-1))
        
            board[0][move - 1] = "O"
        
    elif move == 4 or move == 5 or move == 6:
        if move == 4:
            validacion_de_ocupacion(1, 0)
            board[1][0] = "O"
        elif move == 5:
            validacion_de_ocupacion(1, 1)
            board[1][1] = "O"
        elif move == 6:
            validacion_de_ocupacion(1, 2)
            board[1][2] = "O"
            
    elif move == 7 or move == 8 or move == 9:
        if move == 7:
            validacion_de_ocupacion(2, 0)
            board[2][0] = "O"
        elif move == 8:
            validacion_de_ocupacion(2, 1)
            board[2][1] = "O"
        elif move == 9:
            validacion_de_ocupacion(2, 2)
            board[2][2] = "O"
            

EnterMove()
DisplayBoard()
EnterMove()
DisplayBoard()
    
