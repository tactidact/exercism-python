"""Atbash Cipher Implmentation"""

from string import ascii_lowercase


def encode(plain_text: str) -> str:
    """
    Encodes plain text using Atbash cipher
    """
    encoding = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])
    ciphered_text = ""
    lc_plain_text = plain_text.lower()
    char_count = 0

    for char in lc_plain_text:
        if char in ascii_lowercase:
            ciphered_text += char.translate(encoding)
            char_count += 1
        elif char.isnumeric():
            ciphered_text += char
            char_count += 1
        if char_count % 5 == 0 and char_count != 0:
            ciphered_text += " "
            char_count = 0

    return ciphered_text.strip()


def decode(ciphered_text: str) -> str:
    """
    Decodes ciphered Atbash text to plain text
    """
    decoding = str.maketrans(ascii_lowercase[::-1], ascii_lowercase)
    plain_text = ""

    for char in ciphered_text:
        if char in ascii_lowercase:
            plain_text += char.translate(decoding)
        elif char.isnumeric():
            plain_text += char

    return plain_text
