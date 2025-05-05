
import hashlib

def hash_password(pwd):
    # encode password string to bytes
    enc_pwd = pwd.encode()
    
    # call the sha256(...) function returns a hash object
    d = hashlib.sha256(enc_pwd)

# generate hexadecimal hash of password string
    hash_hex = d.hexdigest()

    return hash_hex

if __name__ == '__main__':
    pwd = input("Enter password: ")

    print(hash_password(pwd))
