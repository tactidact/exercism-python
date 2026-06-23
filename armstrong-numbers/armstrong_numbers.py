def is_armstrong_number(number):
    digit_count = len(str(number))
    digits = list(str(number))
    sum = 0
    for digit in digits:
        sum += int(digit) ** digit_count
    return number == sum
