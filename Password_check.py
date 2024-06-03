import requests
import hashlib
import sys
#arg=sys.argv[1:]

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

'''def read_req(respons, hash_to_check):
    respons=(line.split(':') for line in respons.text.splitlines())
    for i,count in respons:
        if i==hash_to_check:
            return count
    return 0
'''
def read_req(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0
    
def pwned_api_check(password):
    #print(hashlib.sha1(password.encode('UTF-8')).hexdigest().upper())
    sha1=hashlib.sha1(password.encode('UTF-8')).hexdigest().upper()
    firs_5, tail = sha1[:5], sha1[5:]
    respo=request_api_data(firs_5)
    return read_req(respo,tail)


def main(arg):
    for password in arg:
        #print(password)
        count=pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times... you need to change it...!')
        else:
            print(f'Stick with it {password}')
            
    return 'Done!'
main(sys.argv[1:])
if __name__=='__main__':
    pass