from cryptography.fernet import Fernet
import json
import sys
import os

def writeBytes(filename: str, data: dict) -> None:
    with open(filename, 'wb') as file:
        file.write(data)
        print(f'Saved to {filename}')

if __name__ == '__main__':
    dir_prefix = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    key = Fernet.generate_key()

    try:
        with open(dir_prefix + '/.config/api_key.json', 'rb') as file:
            data = file.read()
        encrypted = Fernet(key).encrypt(data)
        print('Encrpytion successful...')

        writeBytes(dir_prefix + '/.config/key.txt', key)
        writeBytes(dir_prefix + '/.config/secret.txt', encrypted)

        # Set ENV
        with open(dir_prefix + '/.venv/bin/activate', 'a') as file:
            file.write(f'\nexport KEY="{key.decode()}"')
            print('KEY set successful')
            file.write(f'\nexport API_KEY="{encrypted.decode()}"')
            print('API_KEY set successful')
            print('Reactivate venv to use new env...')

    except Exception as err:
        print(f'Encryption failed...\n{err}\nTry again...')
    