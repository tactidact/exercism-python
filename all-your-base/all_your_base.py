def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if not digits or set(digits) == {0}:
        return [0]

    rebased_digits: list = []
    dec_value = 0
    power = len(digits) - 1

    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        dec_value += digit * input_base**power
        power -= 1

    while dec_value > 0:
        quotient, remainder = divmod(dec_value, output_base)
        rebased_digits.append(remainder)
        dec_value = quotient
    rebased_digits.reverse()

    return rebased_digits
