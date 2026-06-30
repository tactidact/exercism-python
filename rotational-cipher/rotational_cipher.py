def rotate(text, key):
    rotated_text = str()
    for char in text:
        if char.isalpha():
            if char.islower():
                rotated_char = chr((ord(char) + key - 97) % 26 + 97)
                rotated_text += rotated_char
            else:
                rotated_char = chr((ord(char) + key - 65) % 26 + 65)
                rotated_text += rotated_char
        else:
            rotated_text += char
    return rotated_text


if __name__ == "__main__":
    print(rotate("The quick brown fox jumps over the lazy dog.", 13))
