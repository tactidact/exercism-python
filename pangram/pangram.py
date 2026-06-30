def is_pangram(sentence):
    alphabet = {chr(num) for num in range(97, 123)}
    sentence_set = {char for char in sentence.lower() if char in alphabet}
    return alphabet == sentence_set
