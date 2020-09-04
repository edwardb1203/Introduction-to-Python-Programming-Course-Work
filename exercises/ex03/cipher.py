"""Advanced Decryption and Encryption device!"""
__author__ = "730312903"

A_ASCII_NUMBER: int = 97
A_ASCII_NUMBER_UP: int = 65
LETTERS_ALPHABET: int = 26
LETTER_SHIFT: int = 1


def encode_char(letter: str) -> str:
    """Encodes lettter given +1 shift to the right in alphabet."""
    lower_letter: str = letter.lower()
    if letter == lower_letter:
        ascii_code: int = ord(letter)
        normalized_code: int = ascii_code - A_ASCII_NUMBER
        encoded_code: int = (normalized_code + LETTER_SHIFT) % LETTERS_ALPHABET + A_ASCII_NUMBER
        encoded_letter: str = chr(encoded_code)
        return encoded_letter
    else: 
        ascii_code2: int = ord(letter)
        normalized_code2: int = ascii_code2 - A_ASCII_NUMBER_UP
        encoded_code2: int = (normalized_code2 + LETTER_SHIFT) % LETTERS_ALPHABET + A_ASCII_NUMBER_UP
        encoded_letter2: str = chr(encoded_code2)
        return encoded_letter2


def encode_str(phrase: str) -> str:
    """Encodes a phrase by moving each letter +1 right in alphabet."""
    i: int = 0
    encrypted_chr: str = ""
    while i < len(phrase):
        individ_ltr: str = phrase[i]
        encrypted_chr += encode_char(individ_ltr)
        i = i + 1
    return encrypted_chr


def decode_char(character: str) -> str:
    """Decodes an encoded letter by shifting it back left -1."""
    character_lower: str = character.lower()
    if character == character_lower:
        ascii_code3: int = ord(character)
        normalized_code3: int = ascii_code3 - A_ASCII_NUMBER
        decoded_code: int = (normalized_code3 - LETTER_SHIFT) % LETTERS_ALPHABET + A_ASCII_NUMBER
        decoded_character: str = chr(decoded_code)
        return decoded_character
    else:
        ascii_code4: int = ord(character)
        normalized_code4: int = ascii_code4 - A_ASCII_NUMBER_UP
        decoded_code2: int = (normalized_code4 - LETTER_SHIFT) % LETTERS_ALPHABET + A_ASCII_NUMBER_UP
        decoded_character2: str = chr(decoded_code2)
        return decoded_character2


def decode_str(word: str) -> str:
    """Decodes a word by moving each letter -1 left in alphabet."""
    i: int = 0
    decrypted_ltr: str = ""
    while i < len(word):
        letter2: str = word[i]
        decrypted_ltr += decode_char(letter2)
        i = i + 1
    return decrypted_ltr