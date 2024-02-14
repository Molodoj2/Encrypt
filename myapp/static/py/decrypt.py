# decrypt.py
from cryptography.fernet import Fernet
import ast
import base64

from myapp.static.py.crypt.alphabet import ukrainian_alphabet_upper
from myapp.static.py.crypt.alphabet import russian_alphabet_upper
from myapp.static.py.crypt.alphabet import english_alphabet_upper
from myapp.static.py.crypt.alphabet import morse_code_dict
from myapp.static.py.crypt.alphabet import Homomorphism_alphabet

from myapp.static.py.crypt.Caesar import caesar_decrypt


def decrypt_text_source(method, text, decrypted_key):
    # encrypt Hash-methods
    if method in {'SHA-1', 'SHA-224', 'SHA-256', 'SHA-384', 'SHA-512', 'MD5'}:
        decrypted_text = f"Розшифрування не підтримується для хеш-функцій зокрема для {method}, оскільки вони є однобічними (необоротніми)"


    elif method == 'Fernet':
        text_bytes = ast.literal_eval(text)
        key = decrypted_key.strip("b'").encode()
        decrypted_text = Fernet(key).decrypt(text_bytes).decode('utf-8')

    # encrypt Caesar
    elif method == 'Caesar (Latin)':
        alphabet = english_alphabet_upper
        alphabet_str = ''.join(alphabet)
        decrypted_text = caesar_decrypt(alphabet_str, text, int(decrypted_key))
    elif method == 'Caesar (Cyrillic ukr)':
        alphabet = ukrainian_alphabet_upper
        alphabet_str = ''.join(alphabet)
        decrypted_text = caesar_decrypt(alphabet_str, text, int(decrypted_key))
    elif method == 'Caesar (Cyrillic rus)':
        alphabet = russian_alphabet_upper
        alphabet_str = ''.join(alphabet)
        decrypted_text = caesar_decrypt(alphabet_str, text, int(decrypted_key))

    elif method == 'Morse Code (Latin)':
        morse_code = text.strip()
        morse_code_words = morse_code.split('   ')
        decrypted_text = ''
        for morse_word in morse_code_words:
            morse_letters = morse_word.split()
            for morse_letter in morse_letters:
                for letter, code in morse_code_dict.items():
                    if code == morse_letter:
                        decrypted_text += letter
                        break
            decrypted_text += ' '
            decrypted_text.strip()

    # encrypt Conversion
    elif method == 'Binary':
        decrypted_text = ''.join(chr(int(binary, 2)) for binary in text.split(' '))
    elif method == 'Base64':
        base64_bytes = text.encode('utf-8')
        message_bytes = base64.b64decode(base64_bytes)
        decrypted_text = message_bytes.decode('utf-8')
    elif method == 'Hexadecimal (Latin)':
        decrypted_text = bytes.fromhex(text).decode('utf-8')
    elif method == 'Octal':
        decrypted_text = ''.join(chr(int(char, 8)) for char in text.split())
    elif method == 'Decimal':
        decrypted_text = ''.join(chr(int(char)) for char in text.split())


    elif method == 'Homomorphism (Cyrillic rus)':
        decrypted_text = ''

        codes = text.split()
        for code in codes:
            found = False
            for char, char_codes in Homomorphism_alphabet.items():
                if code in char_codes:
                    decrypted_text += char
                    found = True
                    break

            if not found:
                decrypted_text += code

    else:
        return "Метод розшифрування не підтримується або відсутній ключ"

    return decrypted_text
