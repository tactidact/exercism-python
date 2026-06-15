def square(number):
    if 1 <= number <= 64:
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")


def total():
    total_grains = 0
    for number in range(1, 65):
        total_grains += square(number)
    return total_grains
