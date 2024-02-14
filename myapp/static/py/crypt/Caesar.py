def caesar_encrypt(alphabet, text, decrypted_key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base_index = alphabet.upper().index(char)
                encrypted_text += alphabet.upper()[(base_index + decrypted_key) % len(alphabet)]
            else:
                base_index = alphabet.lower().index(char)
                encrypted_text += alphabet.lower()[(base_index + decrypted_key) % len(alphabet)]
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(alphabet, text, decrypted_key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                base_index = alphabet.upper().index(char)
                decrypted_text += alphabet.upper()[(base_index - decrypted_key) % len(alphabet)]
            else:
                base_index = alphabet.lower().index(char)
                decrypted_text += alphabet.lower()[(base_index - decrypted_key) % len(alphabet)]
        else:
            decrypted_text += char
    return decrypted_text
