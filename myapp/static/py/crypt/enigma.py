rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

rotor1_start = 0
rotor2_start = 0
rotor3_start = 0

plugboard = {"A": "B", "C": "D", "E": "F", "G": "H", "I": "J", "K": "L", "M": "N", "O": "P", "Q": "R", "S": "T",
             "U": "V", "W": "X", "Y": "Z"}

def enigma(text):
    global rotor1_start, rotor2_start, rotor3_start
    text = text.upper().replace(" ", "")
    encrypted_text = []
    for char in text:
        char = plugboard.get(char, char)
        rotor1_start = (rotor1_start + 1) % 26
        if rotor1_start == 0:
            rotor2_start = (rotor2_start + 1) % 26
            if rotor2_start == 0:
                rotor3_start = (rotor3_start + 1) % 26

        char = rotor1[(ord(char) - 65 + rotor1_start) % 26]
        char = rotor2[(ord(char) - 65 + rotor2_start) % 26]
        char = rotor3[(ord(char) - 65 + rotor3_start) % 26]

        char = reflector[(ord(char) - 65) % 26]

        char = chr((rotor3.index(char) - rotor3_start + 26) % 26 + 65)
        char = chr((rotor2.index(char) - rotor2_start + 26) % 26 + 65)
        char = chr((rotor1.index(char) - rotor1_start + 26) % 26 + 65)

        char = plugboard.get(char, char)

        encrypted_text.append(char)

    encrypted_text_str = "".join(encrypted_text)

    return encrypted_text_str
def decrypt_enigma(text):
    global rotor1_start, rotor2_start, rotor3_start
    text = text.upper().replace(" ", "")
    decrypted_text = []
    for char in text:
        char = plugboard.get(char, char)

        # Reverse the rotor movements
        rotor1_start = (rotor1_start - 1) % 26
        if rotor1_start == 25:
            rotor2_start = (rotor2_start - 1) % 26
            if rotor2_start == 25:
                rotor3_start = (rotor3_start - 1) % 26

        # Decryption steps through rotors and reflector
        char = chr((rotor1.index(char) - rotor1_start + 26) % 26 + 65)
        char = chr((rotor2.index(char) - rotor2_start + 26) % 26 + 65)
        char = chr((rotor3.index(char) - rotor3_start + 26) % 26 + 65)

        char = reflector[(ord(char) - 65) % 26]

        char = rotor3[(rotor3.index(char) + rotor3_start) % 26]
        char = rotor2[(rotor2.index(char) + rotor2_start) % 26]
        char = rotor1[(rotor1.index(char) + rotor1_start) % 26]

        char = plugboard.get(char, char)

        decrypted_text.append(char)

    decrypted_text_str = "".join(decrypted_text)

    return decrypted_text_str
encrypted = enigma("Huj w dupe u jobanycz kacapiw")
print("Encrypted Text:", encrypted)

decrypted = decrypt_enigma(encrypted)
print("Decrypted Text:", decrypted)


