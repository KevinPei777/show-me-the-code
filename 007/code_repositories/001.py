from string import ascii_letters, digits
from random import choices


def make_activation_code():
    """
    ascii_letters = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    digits = '0123456789',
    'k' is the length for code
    """
    code = ''.join(choices(ascii_letters+digits, k=15))
    return code


if __name__ == '__main__':
    results = []
    for i in range(200):
        result_code = make_activation_code()
        results.append(result_code)
    print(results)
