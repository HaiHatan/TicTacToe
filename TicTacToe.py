bord = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


# A double for loop to print the bord nicely
def print_bord():
    for i in range(3):
        for j in range(3):
            if '_' in bord[i][j]:
                if j < 2:
                    print('   ', end='|')
                else:
                    print('   ')
            elif "O" in bord[i][j]:
                if j < 2:
                    print(' O ', end='|')
                else:
                    print(' O ')
            elif "X" in bord[i][j]:
                if j < 2:
                    print(' X ', end='|')
                else:
                    print(' X ')
            else:
                print("PANIC")
        if i < 2:
            print('------------')
        else:
            print()


# 0 = player 1, 1 = player 2, 2 = player 1 vs comp
def player_input(player):
    while True:
        if player == 0:
            playerInput = input("Player One enter a valid X location:")
            if test_input(playerInput):
                location = [int(playerInput[0]), int(playerInput[1])]
                if "_" in bord[location[0]][location[1]]:
                    break
                else:
                    print("Location is occupied")
            else:
                print("Invalid location")

        elif player == 1:
            playerInput = input("Player Two enter a valid O location:")
            if test_input(playerInput):
                location = [int(playerInput[0]), int(playerInput[1])]
                if "_" in bord[location[0]][location[1]]:
                    break
                else:
                    print("Location is occupied")
            else:
                print("Invalid location")

        elif player == 2:
            playerInput = input("Player enter a valid X location:")
            if test_input(playerInput):
                location = [int(playerInput[0]), int(playerInput[1])]
                if "_" in bord[location[0]][location[1]]:
                    break
                else:
                    print("Location is occupied")
            else:
                print("Invalid location")
        else:
            print("PANIC")

    return location


# Test if location is free
def set_bord(player, location):
    if player == 0 or player == 2:
        bord[location[0]][location[1]] = "X"
    elif player == 1:
        bord[location[0]][location[1]] = "O"
    else:
        print("PANIC")


# testing for victory by running on the middle raw and column. that way all the possibilities are covered
def test_win():
    victor = -1  # 0 = player 1 (X), 1 = player 2(O), -1 for no victory.
    if "_" not in bord[0][1]:
        if bord[0][1] == bord[1][1] == bord[2][1] or bord[0][1] == bord[0][0] == bord[0][2]:
            if "X" in bord[0][1]:
                victor = 0
                return victor
            elif "O" in bord[0][1]:
                victor = 1
                return victor
    if "_" not in bord[1][1]:
        if bord[1][1] == bord[0][0] == bord[2][2] or bord[1][1] == bord[0][2] == bord[2][0] or bord[1][1] == bord[1][0] == bord[1][2]:
            if "X" in bord[1][1]:
                victor = 0
                return victor
            if "O" in bord[1][1]:
                victor = 1
                return victor
    if "_" not in bord[2][1]:
        if bord[2][1] == bord[2][0] == bord[2][2]:
            if "X" in bord[2][1]:
                victor = 0
                return victor
            if "O" in bord[2][1]:
                victor = 1
                return victor
    if "_" not in bord[1][0]:
        if bord[1][0] == bord[0][0] == bord[2][0]:
            if "X" in bord[1][0]:
                victor = 0
                return victor
            if "O" in bord[2][0]:
                victor = 1
                return victor
    if "_" not in bord[1][2]:
        if bord[1][2] == bord[0][2] == bord[2][2]:
            if "X" in bord[1][2]:
                victor = 0
                return victor
            if "O" in bord[1][2]:
                victor = 1
                return victor
    return victor


# a loop that run on the bord and test there is a free space
def free_space():
    for i in range(3):
        for j in range(3):
            if "_" in bord[i][j]:
                return True
    return False


# function to rest the bord
def reset_bord():
    for i in range(3):
        for j in range(3):
            bord[i][j] = "_"


# testing if the player input is valid
def test_input(playerInput):
    if len(playerInput) != 2:
        flag = False
        return flag
    else:
        if playerInput[0] != "0" and playerInput[0] != "1" and playerInput[0] != "2":
            flag = False
            return flag
        if playerInput[1] != "0" and playerInput[1] != "1" and playerInput[1] != "2":
            flag = False
            return flag
        flag = True
        return flag


# the main function that run the game using the functions.
def run_game():
    game = "Y"
    while game == "Y":
        on = True

        print("welcome to mt Tic Tac Toe game :), Player 1 is X, player 2 is O, Good luck and have fun:")
        print_bord()
        while on:
            game = "N"
            player = 0
            location = player_input(player)
            set_bord(player, location)
            print_bord()
            victor = test_win()
            if victor >= -1:
                if victor == 0:
                    on = False
                    game = input(
                        "Game Over: Player one is the winner!!!!. To start again enter Y (uppercase), to finish game enter anything else:")
                    if game == "Y":
                        reset_bord()
                elif victor == 1:
                    on = False
                    game = input(
                        "Game Over: Player two is the winner!!!!. To start again enter Y, to finish game enter anything else:")
                    if game == "Y":
                        reset_bord()
                        on = False
            if not free_space:
                on = False
                game = input(
                    "Game Over: no more free spaces. Its a tie. To start again enter Y, to finish game enter anything else:")
                if game == "Y":
                    reset_bord()
            if on:
                player = 1
                location = player_input(player)
                set_bord(player, location)
                print_bord()
                victor = test_win()
                if victor >= -1:
                    if victor == 0:
                        on = False
                        game = input(
                            "Game Over: Player one is the winner!!!!. To start again enter Y (uppercase), to finish game enter anything else:")
                        if game == "Y":
                            reset_bord()
                    elif victor == 1:
                        on = False
                        game = input(
                            "Game Over: Player two is the winner!!!!. To start again enter Y, to finish game enter anything else:")
                        if game == "Y":
                            reset_bord()

                if not free_space:
                    game = input(
                        "Game Over: no more free spaces. Its a tie. To start again enter Y, to finish game enter anything else:")
                    if game == "Y":
                        reset_bord()
                        on = False


run_game()
