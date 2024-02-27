import random
import time
import utils


def generate_sequence(n, start_range, end_range):
    return [random.randint(start_range, end_range - 1) for _ in range(n)]


def get_list_from_user(sequence):
    utils.screen_cleaner()
    print(f'A sequence of {len(sequence)} numbers will we shown on screen for 0.7 seconds.\n'
          f'Remember them! then type them back in after they clear.\n'
          f'Press any key to continue...')
    input('')
    print(sequence)
    time.sleep(0.7)
    utils.screen_cleaner()

    user_sequence = []
    for i in range(len(sequence)):
        user_input = input(f"Enter number {i + 1}: ")
        if user_input.isdigit():
            user_sequence.append(int(user_input))
        else:
            user_sequence.append(0)

    return user_sequence


def is_list_equal(list_a, list_b):
    return sorted(list_a) == sorted(list_b)


def play(difficulty):
    print('\nWelcome to the Memory game!\n')
    time.sleep(1.5)
    generated_sequence = generate_sequence(difficulty, 1, 101)
    user_sequence = get_list_from_user(generated_sequence)
    user_won = is_list_equal(generated_sequence, user_sequence)
    if user_won:
        print(f'Congratulations! you remembered the list {generated_sequence} correctly!')
    else:
        print(f'Unfortunately, you remembered the list wrong.\n'
              f'The real list was {generated_sequence}.\n'
              f'You chose {user_sequence}')

    return user_won
