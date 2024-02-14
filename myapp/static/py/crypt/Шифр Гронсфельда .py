from myapp.static.py.crypt.alphabet import russian_alphabet_lower

def gronsfeld_cipher(key, text, alphabet, decrypt=False):
    key_len = len(key)
    alphabet_len = len(alphabet)
    encrypted_text = ''
    for i, char in enumerate(text):
        if char not in alphabet:
            encrypted_text += char
            continue
        shift = int(key[i % key_len])
        if decrypt:
            shift = -shift
        char_index = alphabet.index(char)
        encrypted_text += alphabet[(char_index + shift) % alphabet_len]
    return encrypted_text

# key = '11.12.20.0.4'
key = '11122004'
text = 'клименкоаристарх'

encrypted_text = gronsfeld_cipher(key, text, russian_alphabet_lower)
print("Encrypted text:", encrypted_text)
decrypted_text = gronsfeld_cipher(key, encrypted_text, russian_alphabet_lower, decrypt=True)
print("Decrypted text:", decrypted_text)
