import os

SCORES_FILE_NAME = 'Scores.txt'
BAD_RETURN_CODE = 666


def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_input_number_and_range(input_var, low_range, high_range):
    input_str = str(input_var)
    if not input_str.isdigit():
        return False
    elif int(input_str) < low_range or int(input_str) > high_range:
        return False
    else:
        return True


def request_and_get_int_within_range(text, low_range, high_range):
    chosen_option = ''
    while not check_input_number_and_range(chosen_option, low_range, high_range):
        chosen_option = input(text)
    return int(chosen_option)


def is_float(input_str):
    try:
        float_value = float(input_str)
        return True
    except ValueError:
        return False
