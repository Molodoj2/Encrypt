def encrypt(text, key):
    encrypted_text = ''
    for char in text:
        encrypted_text += '>' + '+' * ord(char) + '.'
    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ''
    bf_code = '[-]'
    index = 0
    for char in encrypted_text:
        if char == '>':
            index += 1
        elif char == '.':
            bf_code += '<' * index + '.'
            index = 0
        elif char == '+':
            bf_code += '>'
        elif char == '-':
            bf_code += '<'
    return bf_code

# Приклад використання:
text = "Hello, World!"
key = None

encrypted_text = encrypt(text, key)
print("Encrypted Text (Brainfuck):", encrypted_text)

decrypted_bf_code = decrypt(encrypted_text, key)
print("Decryption BF code:", decrypted_bf_code)
