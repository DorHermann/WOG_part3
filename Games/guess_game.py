from random import randint
from utils import request_and_get_int_within_range


def generate_number(low, high):
    if low <= high:
        return randint(low, high)


def get_guess_from_user(low_range, high_range):
    request_text = f'Please guess a number between {low_range} and {high_range}:'
    return request_and_get_int_within_range(request_text, low_range, high_range)


def compare_results(users_number, generated_number):
    if users_number == generated_number:
        print(f'Congratulations! the number {users_number} was right. you chose correctly')
        return True
    else:
        print(f'Unfortunately, you chose wrong. the real number was {generated_number}')
        return False


def play(difficulty):
    print('\nWelcome to the Guess Game!\n')
    return compare_results(get_guess_from_user(0, difficulty), generate_number(0, difficulty))
