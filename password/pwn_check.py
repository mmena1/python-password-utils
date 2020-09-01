import hashlib
import sys
import urllib.request

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    with urllib.request.urlopen(url) as response:
        if response.code != 200:
            raise RuntimeError(f'Error fetching: {response.code}, check the api and try again')
        return response.read()

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.decode('utf8').splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

def main(password):
    count = pwned_api_check(password)
    if count:
        print(f'{password} was found {count} times on data breaches... you should never use it!')
    else:
        print(f'{password} was NOT found. Carry on!')
    return 'done!'
