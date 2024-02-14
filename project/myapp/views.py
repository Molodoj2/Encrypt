# views.py
from django.shortcuts import render

from myapp.static.py.encrypt import encrypt_text_source
from myapp.static.py.decrypt import decrypt_text_source
from myapp.static.py.description import description_text


def index(request):
    decrypted_text = None
    encrypted_text = None
    input_text = ""
    decrypted_key = None
    method = None
    description = None

    encryption_methods = ['Hash-methods', 'SHA-1', 'SHA-224', 'SHA-256', 'SHA-384', 'SHA-512', 'MD5',

                          'Historical method', 'Caesar (Latin)', 'Caesar (Cyrillic ukr)', 'Caesar (Cyrillic rus)',
                          'Morse Code (Latin)', 'Homomorphism (Cyrillic rus)',

                          'Conversion', 'Binary', 'Hexadecimal (Latin)', 'Octal', 'Decimal',

                          'Інщі', 'Fernet', 'Base64',
                          'Не працює',
                          'Ротерні', "Enigma (Latin)", 'Безус']

    exclude_methods = ['Hash-methods', 'Historical method', 'Інщі', 'На майбутне', 'Не працює', 'Conversion', 'Ротерні']

    if request.method == 'POST':
        method = request.POST.get('method', '')
        input_text = request.POST.get('input_for_encrypt', '')
        decrypted_key = request.POST.get('encryption_key', '')
        action = request.POST.get('action', '')

        print('method:', method)
        print('input_text:', input_text)
        print('decrypted_key:', decrypted_key)
        print('action:', action)

        if input_text:
            if method and method not in exclude_methods:
                if action == 'encrypt':
                    print('Encrypting...')
                    result = encrypt_text_source(method, input_text)
                    if isinstance(result, tuple):
                        encrypted_text, decrypted_key = result
                        description = description_text(method)
                        print('encrypted_text:', encrypted_text)
                    else:
                        encrypted_text = result
                        description = description_text(method)
                        print('encrypted_text:', encrypted_text)
                elif action == 'decrypt':
                    decrypted_text = decrypt_text_source(method, input_text, decrypted_key)
                    print('decrypted_text: ', decrypted_text)
                    description = description_text(method)

    return render(request, 'test_front.html', {
        'decrypted_text': decrypted_text,
        'encrypted_text': encrypted_text,
        'decrypted_key': decrypted_key,
        'input_text': input_text,
        'method': method,
        'encryption_methods': encryption_methods,
        'exclude_methods': exclude_methods,
        'description': description
    })
