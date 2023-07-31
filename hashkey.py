from cryptography.fernet import Fernet
import json
from typing import Any


def encrypted_json(json_file, key_file = None):
    if key_file == None:
        key = Fernet.generate_key()
        with open('key.key','wb') as file:
            file.write(key)
    else:
        with open(key_file,'rb') as file:
            key = file.read()

    with open(json_file,'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    with open(json_file.split('.')[0]+'_encrypted.json','wb') as f:
        f.write(encrypted)
    
    
def decrypted_json(json_file, key_file):
    with open(key_file,'rb') as file:
        key = file.read()

    with open(json_file,'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    with open(json_file.split('.')[0]+'_decrypted.json','wb') as f:
        f.write(decrypted)
    

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Encrypt or decrypt json file')
    parser.add_argument('-js', '--json_file', type=str, help='json file to encrypt or decrypt')
    parser.add_argument( '-k', '--key_file' , type=str,default=None, help='key file to encrypt or decrypt')

    parser.add_argument('-e', '--encrypt', action='store_true', help='encrypt json file')
    parser.add_argument('-d', '--decrypt', action='store_true', help='decrypt json file')

    args = parser.parse_args()


    if args.encrypt:
        encrypted_json(args.json_file, args.key_file)
    elif args.decrypt:
        decrypted_json(args.json_file, args.key_file)