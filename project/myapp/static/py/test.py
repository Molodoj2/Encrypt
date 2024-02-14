# # Функція для розшифрування повідомлення за допомогою шифру Трисеміуса та ключового слова
# def decrypt_trithemius(ciphertext, keyword):
#     # Таблиця шифру Трисеміуса
#     trithemius_table = [
#         ['Р', 'Е', 'С', 'П', 'У'],
#         ['Б', 'Л', 'И', 'К', 'А'],
#         ['В', 'Г', 'Д', 'Ж', 'З'],
#         ['М', 'Н', 'О', 'Т', 'Ф'],
#         ['Х', 'Ц', 'Ч', 'Ш', 'Щ'],
#         ['Ь', 'Ы', 'Э', 'Ю', 'Я']
#     ]
#
#     # Пошук індексу рядка з ключовим словом у таблиці
#     key_row_index = None
#     for i, row in enumerate(trithemius_table):
#         if all(letter in row for letter in keyword.upper()):
#             key_row_index = i
#             break
#     if key_row_index is None:
#         raise ValueError("Ключове слово не знайдено в таблиці")
#
#     # Розшифрування криптограми
#     plaintext = ''
#     for i, char in enumerate(ciphertext):
#         row_index = i % len(keyword)
#         column_index = trithemius_table[key_row_index].index(char)
#         decrypted_char = trithemius_table[0][column_index]
#         plaintext += decrypted_char
#
#     return plaintext
#
#
# # Криптограма, що потрібно розшифрувати
# ciphertext = "ДЦЩЧБ ХЗЫДУ ИЧЬБЗ ЦУЛШЖ ЧЦЩДО ЛЦЫДЗ ГРЦЧИ ШРЛИГ ДИЧВГ ПОЗПШ ИУАИШ ЗЦЧМГ ЛЦЦЕЛ КБЗМД ГЗЧФЦ ЗЖЧХГ ЛЦДУИ ЦЛД"
# # Ключове слово для розшифрування
# keyword = "РЕСПУБЛИКА"
#
# # Розшифрування повідомлення
# plaintext = decrypt_trithemius(ciphertext, keyword)
# print("Розшифроване повідомлення:", plaintext)
