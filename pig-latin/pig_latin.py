import re


def translate(text):
    words = text.split()
    updated_words = []

    pattern_1 = r"^[aeiou]|^(xr)|^(yt)"
    pattern_2 = r"^[^aeiou]+"
    pattern_3 = r"^[^aeiou]*(qu)"
    pattern_4 = r"^[^aeiou]+y"

    # rule 1
    for word in words:
        # rule 1
        if re.match(pattern_1, word):
            updated_word = word + "ay"
            updated_words.append(updated_word)
            continue

        # rule 4
        match_obj = re.match(pattern_4, word)
        if match_obj:
            updated_word = (
                "y" + re.sub(pattern_4, "", word) + match_obj.group(0)[:-1] + "ay"
            )
            updated_words.append(updated_word)
            continue

        # rule 3
        match_obj = re.match(pattern_3, word)
        if match_obj:
            updated_word = re.sub(pattern_3, "", word) + match_obj.group(0) + "ay"
            updated_words.append(updated_word)
            continue

        # rule 2
        match_obj = re.match(pattern_2, word)
        if match_obj:
            updated_word = re.sub(pattern_2, "", word) + match_obj.group(0) + "ay"
            updated_words.append(updated_word)
            continue

    return " ".join(updated_words)


if __name__ == "__main__":
    print(translate("rhythm"))
