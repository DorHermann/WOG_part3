from random import randint
from currency_converter import CurrencyConverter
from utils import is_float


def get_current_dollar_to_shekel_currency():
    convertor = CurrencyConverter()
    exchange_rate = convertor.convert(1, 'USD', 'ILS')
    if isinstance(exchange_rate, (float, int)):
        print(f"The exchange rate from is: {exchange_rate}")
        return exchange_rate
    else:
        print(f"Error: {exchange_rate}")
        return 0


def get_money_interval(difficulty, dollar_amount):
    shekel_value = dollar_amount * get_current_dollar_to_shekel_currency()
    return {'dollar_amount': dollar_amount,
            'value': shekel_value,
            'low_value': shekel_value - (10 - difficulty),
            'high_value': shekel_value + (10 - difficulty)}


def get_guess_from_user(dollar_amount):
    user_guess = ''
    while not is_float(user_guess):
        user_guess = input(f'Please guess the converted value of {dollar_amount} Dollars into NIS according to the '
                           f'current currency:')
    return float(user_guess)


def compare_results(player_guessed_value, value_interval):
    print(f'The actual value of {value_interval["dollar_amount"]} Dollars is {value_interval["value"]} Shekels')
    if value_interval['low_value'] <= player_guessed_value <= value_interval['high_value']:
        print(f'Congratulations! your guess of {player_guessed_value} Shekels was in range.')
        return True
    else:
        print(f'Unfortunately, your guess of {player_guessed_value} Shekels was out range.')
        return False


def play(difficulty):
    print('\nWelcome to the currency roulette game\n')
    dollar_amount = randint(1, 100)
    return compare_results(get_guess_from_user(dollar_amount), get_money_interval(difficulty, dollar_amount))
