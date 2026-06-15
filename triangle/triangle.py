def equilateral(sides):
    if 0 not in sides and sides[0] == sides[1] and sides[1] == sides[2]:
        return True

    return False


def isosceles(sides):
    if sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]:
        if (
            sides[0] + sides[1] >= sides[2]
            and sides[1] + sides[2] >= sides[0]
            and sides[2] + sides[0] >= sides[1]
        ):
            return True

    return False


def scalene(sides):
    if sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0]:
        if (
            sides[0] + sides[1] >= sides[2]
            and sides[1] + sides[2] >= sides[0]
            and sides[2] + sides[0] >= sides[1]
        ):
            return True

    return False
