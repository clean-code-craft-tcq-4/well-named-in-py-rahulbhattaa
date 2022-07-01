from Colour_code import *


def colour_codes_mapper():
    colour_codes = []
    pair_number = 1
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            colour_codes.append(list((pair_number, major_color, minor_color)))
            pair_number = pair_number + 1
    return colour_codes


def print_manual():
    colour_codes = colour_codes_mapper()
    for colour_code in colour_codes:
        print(colour_code)
