from string import ascii_lowercase


def is_isogram(phrase):
    letters = [char for char in phrase.lower() if char in ascii_lowercase]
    return len(letters) == len(set(letters))
