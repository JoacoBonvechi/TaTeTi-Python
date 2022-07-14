def DisplayBoard(board):
    print(board[0],board[1],board[2], sep="\n")

def EnterMove(board):
    move = int(input("Ingresa tu movimiento, humano "))
    while move > 9 or move < 1:
        move = int(input("Eres idiota humano? Ingresa un movimiento valido "))
    
    def validacion_de_ocupacion(fila, columna):
        if board[fila][columna] == "O" or board[fila][columna] == "X":
            print("Este casillero esta ocupado, ingresa otro humano")
            return True
            
    if move == 1 or move == 2 or move == 3:
            if validacion_de_ocupacion(0,(move-1)):
                return EnterMove(board)
        
            board[0][move - 1] = "O"
        
    elif move == 4 or move == 5 or move == 6:
        if move == 4:
            if validacion_de_ocupacion(1, 0):
                return EnterMove(board)
            board[1][0] = "O"
        elif move == 5:
            if validacion_de_ocupacion(1, 1):
                return EnterMove(board)
            board[1][1] = "O"
        elif move == 6:
            if validacion_de_ocupacion(1, 2):
                return EnterMove(board)
            board[1][2] = "O"
            
    elif move == 7 or move == 8 or move == 9:
        if move == 7:
            if validacion_de_ocupacion(2, 0):
                return EnterMove(board)
            board[2][0] = "O"
        elif move == 8:
            if validacion_de_ocupacion(2, 1):
                return EnterMove(board)
            board[2][1] = "O"
        elif move == 9:
            if validacion_de_ocupacion(2, 2):
                return EnterMove(board)
            board[2][2] = "O"
            
def MakeListOfFreeFields(board):
    free_fields = []
    for i in board:
        for j in i:
            if j != "X" and j != "O":
                elem = j
                free_fields.append(((board.index(i)+1) , (i.index(elem)+1)))
    print(free_fields)

def VictoryFor(sign, board):
    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            print("Gano por linea horizontal",sign)
            return True
    for i in range(3):
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            print("Gano por linea vertical",sign)
            return True

    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        print("Gano por linea cruzada izq a der",sign)
        return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        print("Gano por linea cruzada der a izq",sign)
        return True
    return False
def VictoryForSome(board):
    if VictoryFor("X", board) == True:
        return True
    elif VictoryFor("O", board) == True:
        return True
    else:
        return False
def DrawMove(board):
    from random import randrange
    
    move = randrange(1,10)
    def validacion_de_ocupacion(fila, columna):
        if board[fila][columna] == "O" or board[fila][columna] == "X":
            print("Hhmmmm")
            return True

    if move == 1 or move == 2 or move == 3:
            if validacion_de_ocupacion(0,(move-1)):
                return DrawMove(board)
            print("Mi turno >:)")
            board[0][move - 1] = "X"
        
    elif move == 4 or move == 5 or move == 6:
        if move == 4:
            if validacion_de_ocupacion(1, 0):
                return DrawMove(board)
            print("Mi turno >:)")
            board[1][0] = "X"
        elif move == 5:
            if validacion_de_ocupacion(1, 1):
                return DrawMove(board)
            print("Mi turno >:)")
            board[1][1] = "X"
        elif move == 6:
            if validacion_de_ocupacion(1, 2):
                return DrawMove(board)
            print("Mi turno >:)")
            board[1][2] = "X"
            
    elif move == 7 or move == 8 or move == 9:
        if move == 7:
            if validacion_de_ocupacion(2, 0):
                return DrawMove(board)
            print("Mi turno >:)")
            board[2][0] = "X"
        elif move == 8:
            if validacion_de_ocupacion(2, 1):
                return DrawMove(board)
            print("Mi turno >:)")
            board[2][1] = "X"
        elif move == 9:
            if validacion_de_ocupacion(2, 2):
                return DrawMove(board)
            print("Mi turno >:)")
            board[2][2] = "X"
def Jugar_Ta_Te_Ti():
    board = [[1 + i for i in range(3)]for i in range(3)]
    for i in range(0,3):
        j = 4
        a = 7
        board[1][i] = i + j
        board[2][i] = i + a
        j -= 1
        a -= 1

        
    while True:
        print("Jugemos un juego humano >:)")
        DrawMove(board)
        DisplayBoard(board)
        EnterMove(board)
        DrawMove(board)
        DisplayBoard(board)
        EnterMove(board)
        DrawMove(board)
        DisplayBoard(board)
        gano = VictoryForSome(board)
        if gano:
            DisplayBoard(board)
            break
        EnterMove(board)
        gano = VictoryForSome(board)
        if gano:
            DisplayBoard(board)
            break
        DrawMove(board)
        DisplayBoard(board)
        gano = VictoryForSome(board)
        if gano:
            DisplayBoard(board)
            break
        EnterMove(board)
        gano = VictoryForSome(board)
        if gano:
            DisplayBoard(board)
            break
        DrawMove(board)
        gano = VictoryForSome(board)
        if gano:
            DisplayBoard(board)
            break
        DisplayBoard(board)
        print("Empate humano...")
        break
    otra = input("Quieres jugar de nuevo? si o no ")
    if otra == "si":
        Jugar_Ta_Te_Ti()
    else:
        return
    
Jugar_Ta_Te_Ti()
    
