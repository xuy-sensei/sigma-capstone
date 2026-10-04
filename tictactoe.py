import random as rd

game_board = [

    [" ", " ", " ", " ", "1", " ", " ", " ", "2", " ", " ", " ", "3", " ", " "],
    [" ", " ", "+", "-", "-", "-", "+", "-", "-", "-", "+", "-", "-", "-", "+"],
    ["1", " ", "|", " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "|"],
    [" ", " ", "+", "-", "-", "-", "+", "-", "-", "-", "+", "-", "-", "-", "+"],
    ["2", " ", "|", " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "|"],
    [" ", " ", "+", "-", "-", "-", "+", "-", "-", "-", "+", "-", "-", "-", "+"],
    ["3", " ", "|", " ", " ", " ", "|", " ", " ", " ", "|", " ", " ", " ", "|"],
    [" ", " ", "+", "-", "-", "-", "+", "-", "-", "-", "+", "-", "-", "-", "+"],

]

game_board_mapped_coords = {
    "1,1": (2, 4), "2,1": (2, 8), "3,1": (2, 12),
    "1,2": (4, 4), "2,2": (4, 8), "3,2": (4, 12),
    "1,3": (6, 4), "2,3": (6, 8), "3,3": (6, 12)
}

# will map what symbol the player chose to player in the future (WIP)
symbol_to_player = {}

wincon_list = [
    # Horizontal wincons
    [(2, 4), (2, 8), (2, 12)],
    [(4, 4), (4, 8), (4, 12)],
    [(6, 4), (6, 8), (6, 12)],

    # Vertical wincons
    [(2, 4), (4, 4), (6, 4)],
    [(2, 8), (4, 8), (6, 8)],
    [(2, 12), (4, 12), (6, 12)],

    # Diagonal wincons
    [(2, 4), (4, 8), (6, 12)],
    [(2, 12), (4, 8), (6, 4)]
]


def check_for_wincon(symbol: str) -> bool:
    """
    Function which compares game board state to list of possible win conditions.
    Returns boolean depending on whether win con is present. 
    """

    for row in wincon_list:
        for col in row:
            x, y = col
            if game_board[x][y] != symbol:
                row_correct = False
                break
            else:
                row_correct = True
        if row_correct == True:
            break
    return row_correct


def print_board() -> None:
    """Function which prints the game board."""

    for row in game_board:
        for col in row:
            print(col, end="")
        print()


def choose_mode() -> int:
    """
    Function which lets user choose which mode they would like to play and checks for invalid input.
    1 - singleplayer
    2 - multiplayer
    """

    mode = input("Pick mode: ")

    # checks here for valid input (WIP)

    return int(mode)


def mp_names() -> tuple[str, str]:
    """
    Function which lets user decide their name
    If no input is given, default names are used.
    Returns names as strings in tuple form. 
    """

    name1 = input("Player 1 name? ")
    name2 = input("Player 2 name? ")
    if not name1:
        name1 = "Player 1"
    if not name2:
        name2 = "Player 2"
    return name1, name2


def make_move(x: str, y: str, symbol: str) -> None:
    """ Function which places players symbol on the game board using mapped coordinates (from user input to actual). """
    actual_x, actual_y = game_board_mapped_coords[f"{x},{y}"]
    game_board[actual_x][actual_y] = symbol


def select_coordinate(axis: str) -> str:
    """
    Function which asks the user to pick a coordinate between 1-3 on axis.
    Keeps asking for coordinate if it is out of bounds.
    Returns number as STRING not INT.
    """

    while True:
        num = input(f"{axis}: ")
        if int(num) > 3 or int(num) < 1:
            print("Please enter valid coordinate.")
            continue
        else:
            return num


def run_mp_game(plr1: str, plr2: str, first: str) -> None:
    """
    Main function that runs the majority of the game, responsible for:
    - Getting user input to make move by calling select_coordinate function
    - Checking if target spot is already occupied
    - Making a move by calling make_move function
    - Alternating turns between players
    - Continuing the game until win condition met
    - Printing winner message.
    """

    current_turn = first

    while True:
        print(f"{current_turn} please make your move.")
        print("Please type the column (X) followed by the row (Y) of the coordinate you'd like to place your piece.")
        print_board()
        x = select_coordinate("X")
        y = select_coordinate("Y")

        actual_x, actual_y = game_board_mapped_coords[f"{x},{y}"]

        if game_board[actual_x][actual_y] != " ":
            print(game_board[int(x)][int(y)])
            print("Space is already occupied, please give a different coordinate.")
            continue

        if current_turn == plr1:
            symbol = "X"
            make_move(x, y, symbol)
            win = check_for_wincon(symbol)
            if win:
                break
            current_turn = plr2
        elif current_turn == plr2:
            symbol = "O"
            make_move(x, y, symbol)
            win = check_for_wincon(symbol)
            if win:
                break
            current_turn = plr1

        if win == True:
            break

    print_board()
    print(f"{current_turn} won the game!")


def initialise_game():
    """
    Function which 'initialises' the game, a menu per se. 
    Allows user to pick mode and decides who goes first.
    """

    print("~~~~~~~~~~~~~~~ Hello! ~~~~~~~~~~~~~~~")
    print("Welcome to Tic Tac Toe! A classic game!")
    print("Please select a game mode: ")
    print("1 - Singleplayer")
    print("2 - Multiplayer")

    mode = choose_mode()

    if mode == 1:
        raise Exception("Mode not implemented yet - Sorry :(")
    if mode == 2:
        plr1, plr2 = mp_names()

        num = rd.randint(0, 100)
        if num >= 50:
            first = plr1
        else:
            first = plr2

        run_mp_game(plr1, plr2, first)


initialise_game()
