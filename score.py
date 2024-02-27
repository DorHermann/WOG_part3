from utils import SCORES_FILE_NAME


def add_score(difficulty):
    try:
        file = open(SCORES_FILE_NAME, 'r')
        current_value = int(file.read().strip())
    except FileNotFoundError:
        current_value = 0

    new_value = current_value + int(difficulty) * 3 + 5

    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(new_value))


def get_score():
    current_value = ''
    try:
        file = open(SCORES_FILE_NAME, 'r')
        current_value = int(file.read().strip())
    except FileNotFoundError:
        print("Result file not found")
        raise FileNotFoundError
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return current_value
