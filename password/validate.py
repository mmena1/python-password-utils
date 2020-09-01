import re
import sys

from collections import namedtuple
from functools import reduce

from .pwn_check import pwned_api_check

DEFAULT_PASSWORD_PATTERN = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[-_@.!])[A-Za-z\d\-_@.!]{8,}$'

def validate(password, **kwargs):
    final_pattern = ''
    if kwargs:
        initial_pattern = '(?=(?:.*[a-z])*)|(?=(?:.*[A-Z])*)|(?=(?:.*\d)*)|(?=(?:.*[-_@.!])*)|[A-Za-z\d\-_@.!]|{8,}'
        Pattern = namedtuple('Pattern', ['lowercase', 'uppercase', 'numbers', 'symbols', 'chars', 'length'])
        pattern = Pattern._make(initial_pattern.split('|'))
        min_lowercase = kwargs.get('lowercase')
        min_uppercase = kwargs.get('uppercase')
        min_numbers = kwargs.get('numbers')
        min_symbols = kwargs.get('symbols')
        min_length = kwargs.get('length')
        if min_lowercase:
            pattern = pattern._replace(
                # Using the old way, format: 
                # lowercase='{}{{{},}})'.format(pattern.lowercase[-2], min_lowercase)
                lowercase=f'{pattern.lowercase[:-2]}{{{min_lowercase},}})'
            )
        if min_uppercase:
            pattern = pattern._replace(
                uppercase=f'{pattern.uppercase[:-2]}{{{min_uppercase},}})'
            )
        if min_numbers:
            pattern = pattern._replace(
                numbers=f'{pattern.numbers[:-2]}{{{min_numbers},}})'
            )
        if min_symbols:
            pattern = pattern._replace(
                symbols=f'{pattern.symbols[:-2]}{{{min_symbols},}})'
            )
        if min_length:
            pattern = pattern._replace(length=f'{{{min_length},}}')

        final_pattern = f'{reduce(lambda a,b : a+b, pattern)}'
    else:
        final_pattern = DEFAULT_PASSWORD_PATTERN
    return bool(re.fullmatch(final_pattern, password))

if __name__ == "__main__":
    password = generate(50, include_numbers=True, include_uppercase=True, include_symbols=True)
    while pwned_api_check(password):
        password = generate(50, include_numbers=True, include_uppercase=True, include_symbols=True)
    sys.exit(password)