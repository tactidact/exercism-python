def is_valid(isbn):
    digits = []
    for char in isbn:
        if char.isnumeric():
            digits.append(int(char))
        elif char in {"-", "X"}:
            continue
        else:
            return False

    if isbn and isbn[-1] == "X":
        digits.append(10)

    if len(digits) != 10:
        return False

    digit_sum = 0
    digit_count = 10

    for digit in digits:
        digit_sum += digit * digit_count
        digit_count -= 1

    return not digit_sum % 11
