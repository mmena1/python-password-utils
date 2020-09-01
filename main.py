#!/usr/bin/env python3

import sys

from password.generate import generate
from password.validate import validate
from password.pwn_check import main

if __name__ == "__main__":
    if not sys.argv[1:]:
        while True:
            try:
                text = input(
                    """Select the option you like to run:
                    1) Generate a password
                    2) Validate a password
                    3) Check if password is pwned\n"""
                )
                if text == "1":
                    length = input('How many characters? ')
                    uppercase = input('Should contain uppercase letters? ')
                    numbers = input('Should contain numbers? ')
                    symbols = input('Should contain special characters? ')
                    print(generate(
                        int(length),
                        include_uppercase=uppercase,
                        include_numbers=numbers,
                        include_symbols=symbols
                    ))
                    break
                elif text == "2":
                    length = input('Minimum length? ')
                    lowercase = input('How many lowercase letters? ')
                    uppercase = input('How many uppercase letters? ')
                    numbers = input('How many numbers? ')
                    symbols = input('How many symbols? ')
                    password = input('Enter the password: ')
                    validated = validate(
                        password, 
                        lowercase=lowercase,
                        uppercase=uppercase,
                        numbers=numbers,
                        symbols=symbols,
                        length=length
                    )
                    print('Password valid!') if validated else print('Invalid password!')
                    break
                elif text == "3":
                    main(input('Enter a password: '))
                    break
                else:
                    print("Invalid option. Please try again.")
            except RuntimeError:
                print("There was an error with the API call, please fix it ASAP!")
                raise
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
