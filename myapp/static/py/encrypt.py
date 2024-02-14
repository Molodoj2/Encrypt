# encrypt.py
import hashlib
from cryptography.fernet import Fernet
import random
import base64

from myapp.static.py.crypt.alphabet import ukrainian_alphabet_upper
from myapp.static.py.crypt.alphabet import russian_alphabet_upper
from myapp.static.py.crypt.alphabet import english_alphabet_upper
from myapp.static.py.crypt.alphabet import morse_code_dict
from myapp.static.py.crypt.alphabet import Homomorphism_alphabet

from myapp.static.py.crypt.Caesar import caesar_encrypt

from myapp.static.py.crypt.enigma import enigma


def encrypt_text_source(method, text):
    # encrypt Hash-methods
    if method in {'SHA-1', 'SHA-224', 'SHA-256', 'SHA-384', 'SHA-512', 'MD5'}:
        decrypted_key = None
        encrypted_text = hashlib.new(method, text.encode()).hexdigest()


    elif method == 'Fernet':
        decrypted_key = Fernet.generate_key()
        cipher_suite = Fernet(decrypted_key)
        encrypted_text = cipher_suite.encrypt(text.encode())

    # encrypt Caesar
    elif method == 'Caesar (Latin)':
        alphabet = english_alphabet_upper
        decrypted_key = random.randint(1, 26)
        alphabet_str = ''.join(alphabet)
        encrypted_text = caesar_encrypt(alphabet_str, text, decrypted_key)
    elif method == 'Caesar (Cyrillic ukr)':
        alphabet = ukrainian_alphabet_upper
        decrypted_key = random.randint(1, 33)
        alphabet_str = ''.join(alphabet)
        encrypted_text = caesar_encrypt(alphabet_str, text, decrypted_key)
    elif method == 'Caesar (Cyrillic rus)':
        alphabet = russian_alphabet_upper
        decrypted_key = random.randint(1, 30)
        alphabet_str = ''.join(alphabet)
        encrypted_text = caesar_encrypt(alphabet_str, text, decrypted_key)

    elif method == 'Morse Code (Latin)':
        decrypted_key = None
        text = text.upper()
        encrypted_text = ''
        for char in text:
            if char in morse_code_dict:
                encrypted_text += morse_code_dict[char] + ' '
            elif char == ' ':
                encrypted_text += ' '

    # encrypt Conversion
    elif method == 'Binary':
        decrypted_key = None
        encrypted_text = ' '.join(format(ord(char), '08b') for char in text)
    elif method == 'Base64':
        decrypted_key = None
        message_bytes = text.encode('utf-8')
        base64_bytes = base64.b64encode(message_bytes)
        encrypted_text = base64_bytes.decode('utf-8')
    elif method == 'Hexadecimal (Latin)':
        decrypted_key = None
        encrypted_text = ''.join(hex(ord(char))[2:] for char in text)
    elif method == 'Octal':
        decrypted_key = None
        encrypted_text = ' '.join(format(ord(char), 'o') for char in text)
    elif method == 'Decimal':
        decrypted_key = None
        encrypted_text = ' '.join(str(ord(char)) for char in text)


    elif method == 'Homomorphism (Cyrillic rus)':
        decrypted_key = None
        encrypted_text = ''
        for char in text:
            if char.upper() in Homomorphism_alphabet:
                code = Homomorphism_alphabet[char.upper()]
                encrypted_text += code[random.randint(0, len(code) - 1)] + ' '
            else:
                encrypted_text += char

    elif method == 'Enigma (Latin)':
        decrypted_key = None
        encrypted_text = enigma(text)
    else:
        return "Метод шифрування не підтримується або відсутній ключ"

    return encrypted_text, decrypted_key
