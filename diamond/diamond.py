def rows(letter):
    if letter == "A":
        return [letter]

    output = []
    current_letter_value = 1
    letter_value = ord(letter) - 64
    inner_space = 1
    outer_space = letter_value - 1

    output.append(
        outer_space * " " + chr(current_letter_value + 64) + outer_space * " "
    )
    outer_space -= 1
    current_letter_value += 1

    while current_letter_value <= letter_value:
        output.append(
            outer_space * " "
            + chr(current_letter_value + 64)
            + inner_space * " "
            + chr(current_letter_value + 64)
            + outer_space * " "
        )
        inner_space += 2
        outer_space -= 1
        current_letter_value += 1

    current_letter_value -= 2
    inner_space -= 4
    outer_space += 2

    while current_letter_value > 1:
        output.append(
            outer_space * " "
            + chr(current_letter_value + 64)
            + inner_space * " "
            + chr(current_letter_value + 64)
            + outer_space * " "
        )
        inner_space -= 2
        outer_space += 1
        current_letter_value -= 1

    output.append(
        outer_space * " " + chr(current_letter_value + 64) + outer_space * " "
    )

    return output


if __name__ == "__main__":
    for row in rows("Z"):
        print(row)
