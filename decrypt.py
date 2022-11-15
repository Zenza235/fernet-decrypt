import sys

from cryptography.fernet import Fernet

if __name__ == '__main__':
    filepath = sys.argv[1] # path of file to be encrypted

    print('Enter fernet key: ') # base 64 format
    key = input()
    fernet = Fernet(key)

    with open(filepath, 'rb') as enc_file:
        encrypted = enc_file.read()
    
    decrypted = fernet.decrypt(encrypted)
    with open(filepath, 'wb') as dec_file:
        dec_file.write(decrypted)
    
    print('File decrypted.')


    
