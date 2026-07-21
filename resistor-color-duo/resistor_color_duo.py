def value(colors):
    color_list = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white",
    ]

    return int("".join([str(color_list.index(color)) for color in colors][0:2]))
