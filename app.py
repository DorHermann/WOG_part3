from Games.currency_roulette_game import play as currency_roulette_game_play
from Games.guess_game import play as guess_game_play
from Games.memory_game import play as memory_game_play
from utils import request_and_get_int_within_range, screen_cleaner
from score import add_score, get_score


def welcome():
    user_name = input("Please enter your name: ")
    screen_cleaner()
    print(f'Hi {user_name.strip()} and welcome to the World of Games: The Epic Journey\n'
          f'~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~@~\n')


def get_menu():
    return """Please choose a game to play:
            1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
            2. Guess Game - guess a number and see if you chose like the computer.
            3. Currency Roulette - try and guess the value of a random amount of USD in ILS
            """


def start_play():
    keep_playing = True
    while keep_playing:
        game_chosen = request_and_get_int_within_range(get_menu(), 1, 3)
        print(f'You have chosen game number {game_chosen}')

        difficulty_level = request_and_get_int_within_range('\nselect a difficulty level between 1 and 5:', 1, 5)
        print(f'You have chosen difficulty level {difficulty_level}')

        did_user_win = ''
        match game_chosen:
            case 1:
                did_user_win = memory_game_play(difficulty_level)
            case 2:
                did_user_win = guess_game_play(difficulty_level)
            case 3:
                did_user_win = currency_roulette_game_play(difficulty_level)

        if did_user_win:
            end_msg = "\nGreat! You've won your game.\n"
            add_score(difficulty_level)
            end_msg += f"\nYour total score is :{get_score()}.\n"
        else:
            end_msg = "\nToo bad! You've lost your game.\n"

        if not input(end_msg + 'Press Y to play again:').upper() == 'Y':
            keep_playing = False
        screen_cleaner()

    print('Farewell and Come again.')
