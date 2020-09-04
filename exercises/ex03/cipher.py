"""Advanced Decryption and Encryption device!"""
__author__ = "730312903"

A_ASCII_NUMBER: int = 97
A_ASCII_NUMBER_UP: int = 65
LETTERS_ALPHABET: int = 26
LETTER_SHIFT: int = 1


def encode_char(letter: str) -> str:
    """Encodes lettter given +1 shift to the right in alphabet."""
    letter: str = letter
    lower_letter: str = letter.lower()
    if letter == lower_letter:
        ascii_code: int = ord(letter)
        normalized_code: int = ascii_code - A_ASCII_NUMBER
        encoded_code: int = (normalized_code + LETTER_SHIFT) % LETTERS_ALPHABET + A_ASCII_NUMBER
        encoded_letter: str = chr(encoded_code)
        return encoded_letter
    else: 
        ascii_code: int = ord(letter)
        normalized_code: int = ascii_code - A_ASCII_NUMBER_UP
        encoded_code: int = (normalized_code + LETTER_SHIFT) % LETTERS_ALPHABET + A_ASCII_NUMBER_UP
        encoded_letter: str = chr(encoded_code)
        return encoded_letter


def encode_str(phrase: str) -> str:
    """Encodes a phrase by moving each letter +1 right in alphabet."""
    i: int = 0
    encrypted_chr: str = ""
    while i < len(phrase):
        character: str = phrase[i]
        encrypted_chr += encode_char(character)
        i = i + 1
    return encrypted_chr


def decode_char(character: str) -> str:
    """Decodes an encoded letter by shifting it back left -1."""
    character_lower: str = character.lower()
    if character == character_lower:
        ascii_code: int = ord(character_lower)
        normalized_code: int = ascii_code - A_ASCII_NUMBER
        decoded_code: int = (normalized_code - LETTER_SHIFT) % LETTERS_ALPHABET + A_ASCII_NUMBER
        decoded_character: str = chr(decoded_code)
        return decoded_character
    else:
        ascii_code: int = ord(character_lower)
        normalized_code: int = ascii_code - A_ASCII_NUMBER_UP
        decoded_code: int = (normalized_code - LETTER_SHIFT) % LETTERS_ALPHABET + A_ASCII_NUMBER_UP
        decoded_character: str = chr(decoded_code)
        return decoded_character


def decode_str(word: str) -> str:
    """Decodes a word by moving each letter -1 left in alphabet."""
    i: int = 0
    decrypted_ltr: str = ""
    while i < len(word):
        letter: str = word[i]
        decrypted_ltr += decode_char(letter)
        i = i + 1
    return decrypted_ltr


    if __name__ == "__encode_char__":
        encode_char