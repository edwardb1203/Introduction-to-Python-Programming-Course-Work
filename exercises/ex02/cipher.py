"""Decryption and Encryption device!"""
__author__ = "730312903"

A_ASCII_NUMBER: int = 97
LETTERS_ALPHABET: int = 26
LETTER_SHIFT: int = 1


def encode_char(letter: str) -> str:
    """Encodes lettter given +1 shift to the right in alphabet."""
    letter_lower: str = letter.lower()
    ascii_code: int = ord(letter_lower)
    normalized_code: int = ascii_code - A_ASCII_NUMBER
    encoded_code: int = (normalized_code + LETTER_SHIFT) % LETTERS_ALPHABET + A_ASCII_NUMBER
    encoded_letter: str = chr(encoded_code)
    return encoded_letter


def encode_str(phrase: str) -> str:
    """Encodes a phrase by moving each letter +1 right in alphabet."""
    code_letter_1: str = encode_char(phrase[len(phrase) - 4])
    code_letter_2: str = encode_char(phrase[len(phrase) - 3])
    code_letter_3: str = encode_char(phrase[len(phrase) - 2])
    code_letter_4: str = encode_char(phrase[len(phrase) - 1])
    encoded_phrase: str = (code_letter_1 + code_letter_2 + code_letter_3 + code_letter_4)
    return encoded_phrase


def decode_char(character: str) -> str:
    """Decodes an encoded letter by shifting it back left -1."""
    character_lower: str = character.lower()
    ascii_code: int = ord(character_lower)
    normalized_code: int = ascii_code - A_ASCII_NUMBER
    decoded_code: int = (normalized_code - LETTER_SHIFT) % LETTERS_ALPHABET + A_ASCII_NUMBER
    decoded_character: str = chr(decoded_code)
    return decoded_character


def decode_str(word: str) -> str:
    """Decodes a word by moving each letter -1 left in alphabet."""
    decode_letter_1: str = decode_char(word[len(word) - 4])
    decode_letter_2: str = decode_char(word[len(word) - 3])
    decode_letter_3: str = decode_char(word[len(word) - 2])
    decode_letter_4: str = decode_char(word[len(word) - 1])
    decoded_word: str = (decode_letter_1 + decode_letter_2 + decode_letter_3 + decode_letter_4)
    return decoded_word