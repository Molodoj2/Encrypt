def decrypt_trithemius(ciphertext, key):
    plaintext = ""
    key_size = len(key)
    for char in ciphertext:
        if char == ' ':
            plaintext += ' '
            continue
        for i in range(key_size):
            if char in key[i]:
                row = i
                column = key[i].index(char)
                shift = (row + column) % key_size
                plaintext += key[shift][column]
                break
    return plaintext

key = [
    ['Р', 'Е', 'С', 'П', 'У'],
    ['Б', 'Л', 'И', 'К', 'А'],
    ['В', 'Г', 'Д', 'Ж', 'З'],
    ['М', 'Н', 'О', 'Т', 'Ф'],
    ['Х', 'Ц', 'Ч', 'Ш', 'Щ'],
    ['Ь', 'Ы', 'Э', 'Ю', 'Я']
]

ciphertext = "АНБЧФ ЕБЛЗГ ДФЗЫД УЖЧШЧ БЕЬКБ ДМЧОУ ШЖКЧШ ЛБЛДЦ ЩЧБХЗ ЫДЛДЛ ЛИМЧД ИШМИЧ ЧШМЛШ ИШМЛЦ ЦЧЦЗФ ЕМЗПШ ИУАНБ ЧФЗХД ЖЧЦЩД ОЛЦЫД ЗГРЦЧ ИШДЫЛ ГЧИШЦ ЧИШДД ОЧИША КЦЧИШ Д"

decrypted_text = decrypt_trithemius(ciphertext, key)
print(decrypted_text)
