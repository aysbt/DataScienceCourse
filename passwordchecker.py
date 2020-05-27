import requests
import hashlib #secure hashed message
import sys
def request_api_data(query_char):
    '''We are going to give hashed version of our password'''
    # K anonymity takes first 5 charecter of hashed passwrod
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error Fetching: {res.status_code}, check the the api and try again.')
    return res

def get_response_leaks_count(hashes, hash_to_check):
    #create toplle with hash and count objects
    #print(hashes.text.splitlines())
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    '''We give our actual password we want to check password if it exists in APi response '''
    #hash our passwrod
    shaipassword= hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = shaipassword[:5], shaipassword[5:]
    response = request_api_data(first5_char)
    return get_response_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times.. You should change your password')
        else:
            print(f'{password} was not found... Carry on!')
    return 'done !'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
