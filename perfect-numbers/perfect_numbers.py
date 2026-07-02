def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1 or not isinstance(number, int):
        raise ValueError("Classification is only possible for positive integers.")

    if number == 1:
        return "deficient"

    aliquot_sum = 1
    for potential_divisor in range(2, int(number**0.5) + 1):
        if number % potential_divisor == 0:
            aliquot_sum += potential_divisor
            if potential_divisor != number // potential_divisor:
                aliquot_sum += number // potential_divisor

    if number == aliquot_sum:
        return "perfect"
    if number < aliquot_sum:
        return "abundant"
    if number > aliquot_sum:
        return "deficient"


if __name__ == "__main__":
    print(classify(28))
