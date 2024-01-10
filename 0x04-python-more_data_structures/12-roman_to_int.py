#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if roman_string is not str:
        return 0
    codex = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    total = 0
    for i, j in enumerate(roman_string):
        total += codex[j]
        if i + 1 < len(roman_string):
            if codex[j] < codex[roman_string[i + 1]]:
                total -= (codex[j] * 2)
    return total
