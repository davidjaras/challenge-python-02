# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
ASCII_LOWERCASE = list(string.ascii_lowercase)
ASCII_UPPERCASE = list(string.ascii_uppercase)
DIGITS = list(string.digits)

def generate_password():
    # Start coding here
    len_password = random.randint(8,16)
    password = ''

    password += random.choice(SYMBOLS)
    password += random.choice(ASCII_LOWERCASE)
    password += random.choice(ASCII_UPPERCASE)
    password += random.choice(DIGITS)

    for _ in range(len_password - 4):
        character_set = random.choice([SYMBOLS, ASCII_LOWERCASE, ASCII_UPPERCASE, DIGITS])
        password += random.choice(character_set)
    
    password = list(password)
    random.shuffle(password)
    password = ''.join(password)

    return password


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
