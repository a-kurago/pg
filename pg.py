from typing import Optional, List
import random
import click


LETTERS = 'abcdefghijklmnopqrstuvwxyz'
SPEC_CHARS = '~!@#$%^&*()_+;:?-=.<>'


def random_digit(exclude_similar=False):
    if exclude_similar:
        return str(random.randint(2, 9))
    else:
        return str(random.randint(0, 9))


def random_letter(exclude_similar=False):
    if exclude_similar:
        letters = LETTERS.replace('l', '').replace('o', '')
        return random.choice(letters)
    else:
        return random.choice(LETTERS)


def random_upper_letter(exclude_similar=False):
    if exclude_similar:
        letters = LETTERS.upper().replace('I', '').replace('O', '')
        return random.choice(letters)
    else:
        return random.choice(LETTERS.upper())


def random_spec_char():
    return random.choice(SPEC_CHARS)


def gen_password(length: int,
                 use_digits,
                 use_letters,
                 use_upper_letters,
                 use_spec_characters,
                 exclude_similar):
    password_chars: List[Optional[str]] = [None] * length
    char_classes = []

    if use_digits:
        char_classes.append('d')
    if use_letters:
        char_classes.append('l')
    if use_upper_letters:
        char_classes.append('L')
    if use_spec_characters:
        char_classes.append('s')

    random_char_indexes = random.choices(range(length), k=len(char_classes))

    for char_index, char_class in zip(random_char_indexes, char_classes):
        password_chars[char_index] = char_class

    for i, password_char in enumerate(password_chars):
        if password_char is None:
            password_chars[i] = random.choice(char_classes)

    return gen_password_by_pattern(password_chars, exclude_similar)


def gen_password_by_pattern(pattern, exclude_similar=False):
    password_chars = []
    for p in pattern:
        if p == 'd':
            password_chars.append(random_digit(exclude_similar))
        if p == 'l':
            password_chars.append(random_letter(exclude_similar))
        if p == 'L':
            password_chars.append(random_upper_letter(exclude_similar))
        if p == 's':
            password_chars.append(random_spec_char())

    return ''.join(password_chars)



@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('-n', '--length', 'password_len', default=7, help='Password length')
@click.option('-c', '--count', 'passwords_count', default=8, help='Number of passwords to generate')
@click.option('-d', '--use-digits', is_flag=True)
@click.option('-l', '--use-letters', is_flag=True)
@click.option('-L', '--use-upper-letters', is_flag=True)
@click.option('-s', '--use-special-chars', is_flag=True)
@click.option('-S', '--special-chars-set', default=SPEC_CHARS, show_default=False,
              help='Set of special characters to use in password. Example: @#$%')
@click.option('-e', '--exclude-similar', is_flag=True, default=False, show_default=False,
              help='Exclude similar characters like 0,o,O,1,l,I')
@click.option('-p', '--pattern', 'pattern',
              help='Example: "llddLL". d, l, L, s stands for digit, letter, upper letter, special character')
def main(password_len,
         passwords_count,
         use_digits,
         use_letters,
         use_upper_letters,
         use_special_chars,
         special_chars_set,
         exclude_similar,
         pattern):
    global SPEC_CHARS
    SPEC_CHARS = special_chars_set

    if pattern:
        for letter in pattern:
            if letter not in 'dlLs':
                print('Pattern format error.')
                exit(1)
        for _ in range(passwords_count):
            print(gen_password_by_pattern(pattern, exclude_similar))
        return

    min_pass_len = 0

    if use_digits:
        min_pass_len += 1
    if use_letters:
        min_pass_len += 1
    if use_upper_letters:
        min_pass_len += 1
    if use_special_chars:
        min_pass_len += 1

    if min_pass_len == 0:
        use_digits = True
        use_letters = True
        use_upper_letters = True

    if password_len < min_pass_len:
        print(f'Minimum password length with selected parameters is {min_pass_len}')
        exit(2)

    for _ in range(passwords_count):
        print(gen_password(
            password_len,
            use_digits,
            use_letters,
            use_upper_letters,
            use_special_chars,
            exclude_similar
        ))


if __name__ == '__main__':
    main()
