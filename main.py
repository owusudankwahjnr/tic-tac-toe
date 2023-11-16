my_dict = {
    "A": ['_', '_', '_'],
    "B": ['_', '_', '_'],
    "C": ['_', '_', '_'],
}
ALL_INPUTS = "ABC123"


def display_board():
    print("Welcome to the TIC_TAC_TOE game:")
    print("    1    2    3")
    print(f"A {my_dict['A']}")
    print(f"B {my_dict['B']}")
    print(f"C {my_dict['C']}")


def players_turn(time: int, chosen_cell: str):
    if (time % 2) == 0:
        player_sign = 'X'
    else:
        player_sign = 'O'
    x = int(chosen_cell[1]) - 1
    y = chosen_cell[0].upper()

    my_dict[y][x] = player_sign
    display_board()
    if player_sign == 'X':
        player_sign = 'O'
    else:
        player_sign = 'X'
    return player_sign


display_board()
print("Player 'O' plays first")


def valid_cell(cell_name: str):
    x_input = cell_name[1]
    y_input = cell_name[0].upper()
    is_valid = x_input in ALL_INPUTS and y_input in ALL_INPUTS
    if is_valid:
        x_input = int(x_input) - 1
        return my_dict[y_input][x_input] == "_"

    return False


def is_equal_to_3(x_value: int, o_value: int):
    if x_value == 3:
        print("Player 'X' wins")
        return True
    elif o_value == 3:
        print("Player 'O' wins")
        return True
    return False


def has_won():
    row_A = my_dict["A"]
    row_B = my_dict['B']
    row_C = my_dict['C']
    row_list = [row_A, row_B, row_C]
    column_1 = []
    column_3 = []
    column_2 = []

    for item in row_list:
        x_total = item.count("X")
        o_total = item.count("O")
        any_is_3 = is_equal_to_3(x_total, o_total)
        if any_is_3:
            return True

    for key, value in my_dict.items():
        column_1.append(my_dict[key][0])
        column_2.append(my_dict[key][1])
        column_3.append(my_dict[key][2])

    all_columns = [column_1, column_2, column_3]

    for item in all_columns:
        x_total = item.count('X')
        o_total = item.count('O')
        any_is_3 = is_equal_to_3(x_total, o_total)
        if any_is_3:
            return True

    left_diagonal = [my_dict['A'][0], my_dict['B'][1], my_dict['C'][2]]
    Xs_for_diagonal = left_diagonal.count('X')
    Os_for_diagonal = left_diagonal.count('O')
    any_is_3 = is_equal_to_3(Xs_for_diagonal, Os_for_diagonal)
    if any_is_3:
        return True

    right_diagonal = [my_dict['A'][2], my_dict['B'][1], my_dict['C'][0]]
    Xs_for_diagonal = right_diagonal.count('X')
    Os_for_diagonal = right_diagonal.count('O')
    any_is_3 = is_equal_to_3(Xs_for_diagonal, Os_for_diagonal)
    if any_is_3:
        return True

    return False


for loop_time in range(1, 10):
    user_input = input("Enter a cell name: ")
    cell_is_valid = valid_cell(user_input)

    while not cell_is_valid:
        print("Cell out of range / Cell has been taken")
        user_input = input("Enter a cell name: ")
        cell_is_valid = valid_cell(user_input)

    next_player = players_turn(loop_time, user_input)

    if has_won():
        break
    elif loop_time == 10:
        print("It's a Draw game")
    else:
        print(f"Player {next_player}'s turn:")
