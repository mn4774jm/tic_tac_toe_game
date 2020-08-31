
import re
import random
# regular expression pattern for validation
pattern = re.compile(r'\b[1-9]\b')
# dictionary used for game printing and validation on computer/player turn
game_square_dict = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9}
# used for turn tracking and winner announcement
turn = 'Player'
turn_count = 0

# overarching controller. Responsible for beginning the game, starting the turn_controller, and restarting the program
# when turn controller function completes
def main():
    begin_game()
    print_board()
    turn_controller()
    winner()
    restart()


# controls the flow of user and computer turns.
def turn_controller():
    validated_entry = new_turn()
    add_to_game_board(validated_entry)
    is_win_condition()


# simple start for the user to see
def begin_game():
    print('Welcome to Tic-Tac-Toe!')
    input('Press enter to begin!')


# game board print statements use hard coded patterns for the layout. game_square dictionary is initially populated
# with numbers 1-9 and replaced by either "X" or "O" in the add_to_game_board function after numbers are selected and validated
def print_board():
    print('{:<1}{:^1}{:<2}{:<1}{:^1}{:<2}{:<1}{:^1}{:<1}'.format('_', f'{game_square_dict[1]}', '_|','_',f'{game_square_dict[2]}', '_|','_', f'{game_square_dict[3]}', '_'))
    print('{:<1}{:^1}{:<2}{:<1}{:^1}{:<2}{:<1}{:^1}{:<1}'.format('_', f'{game_square_dict[4]}', '_|','_', f'{game_square_dict[5]}', '_|','_', f'{game_square_dict[6]}', '_'))
    print('{:<1}{:^1}{:<2}{:<1}{:^1}{:<2}{:<1}{:^1}{:<1}'.format(' ', f'{game_square_dict[7]}', ' |',' ', f'{game_square_dict[8]}', ' |',' ', f'{game_square_dict[9]}', ' \n'))


# conditional logic is used to check which turn the game is on. If 'Player' is currently in the turn variable an
# input prompt will be used asking the player to select a number. If 'Computer' is currently stored in turn the
# random.randint function from the random library is used to choose a number 1-9. In either instance the number
# selected will be passed through the number_validation follwed by the move_validation functions before being
# returned to the turn controller.
def new_turn():
    global turn
    if turn == 'Player':
        num_selection = input('Choose a square (1-9): ')
        return move_validation(number_validation(num_selection))
    else:
        return move_validation(number_validation(random.randint(1, 9)))


# regular expression is used to ensure that the only allowed entry is numeric between 1-9. Conversion to string is
# required for pattern matching. if no pattern is found the user is asked to submit a new entry until a match is found.
# When match condition is met the value is returned to turn_controller.
def number_validation(selection):
    mo = pattern.search(str(selection))
    while mo is None:
        selection = input("Please enter a single number 1-9 with no spaces: ")
        mo = pattern.search(selection)
    number_fixed = int(selection)
    return number_fixed



def move_validation(choice):
    global turn
    global turn_count
    mo = pattern.search(str(game_square_dict[choice]))
    if mo is None:
        if turn == 'Player':
            print('Not allowed, Choose an empty square')
            print_board()
            turn_controller()
        elif turn == 'Computer':
            turn_controller()
    else:
        if turn == 'Player':
            turn_count += 1
            return choice
        elif turn == 'Computer':
            turn_count += 1
            return choice


def add_to_game_board(entry):
    global turn
    if turn == 'Player':
        game_square_dict[entry] = 'X'
        print_board()
    elif turn == 'Computer':
        game_square_dict[entry] = 'O'
        print_board()


# conditional logic used to check for game winning combinations. When satisfied winner function called if not a draw
#TODO add else to call for user/computer turn method if no other conditions are met
def is_win_condition():
    global turn
    if turn == 'Player':
        box = 'X'
    else:
        box = 'O'
    if (game_square_dict[1] == box and game_square_dict[2] == box and game_square_dict[3] == box) or \
            (game_square_dict[4] == box and game_square_dict[5] == box and game_square_dict[6] == box) or \
            (game_square_dict[7] == box and game_square_dict[8] == box and game_square_dict[9] == box) or \
            (game_square_dict[1] == box and game_square_dict[4] == box and game_square_dict[7] == box) or \
            (game_square_dict[2] == box and game_square_dict[5] == box and game_square_dict[8] == box) or \
            (game_square_dict[3] == box and game_square_dict[6] == box and game_square_dict[9] == box) or \
            (game_square_dict[1] == box and game_square_dict[5] == box and game_square_dict[9] == box) or \
            (game_square_dict[3] == box and game_square_dict[5] == box and game_square_dict[7] == box):
        return
    elif turn_count == 9:
        print("Aaaand It's a tie!")
        # restart()
    else:
        if turn == 'Player':
            turn = 'Computer'
            print(f'{turn} turn')
            turn_controller()
        else:
            turn = 'Player'
            print(f'{turn} turn')
            turn_controller()


# print winner and call restart function
def winner():
    print(f"{turn} Wins!!!")
    restart()

# ask user if they would like to restart and resets the game board
def restart():
    again = input("Would you like to try again? Enter 'y' or 'n': ")
    while again.lower() != 'y' and again.lower() != 'n':
        again = input("Would you like to try again? Enter 'y' or 'n': ")
    if again == 'y':
        print()
        for i in range(len(game_square_dict)):
            game_square_dict[i+1]=i+1
        main()
    else:
        print('Thanks for playing!')
        exit()



main()