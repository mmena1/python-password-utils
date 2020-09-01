import string

from random import choice, shuffle

def generate(length, **kwargs):
    if len(kwargs) > length:
        raise RuntimeError('The password length cannot be lower then the number of arguments')
    available_chars = string.ascii_lowercase
    password = ''
    if kwargs.get('include_numbers'):
        available_chars += string.digits
        password += choice(string.digits)
    if kwargs.get('include_uppercase'):
        available_chars += string.ascii_uppercase
        password += choice(string.ascii_uppercase)
    if kwargs.get('include_symbols'):
        available_chars += '-_@.!'
        password += choice('-_@.!')
    final_password = password + ''.join([choice(available_chars) for i in range(length - len(password))])
    pass_to_list = list(final_password)
    shuffle(pass_to_list)
    return ''.join(pass_to_list)
