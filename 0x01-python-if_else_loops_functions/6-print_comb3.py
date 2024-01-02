#!/usr/bin/python3
for tens in range(0, 9):
    for ones in range(0, 10):
        if ones == 9 and tens == 8:
            break
        if ones > tens:
            print("{}{}".format(tens, ones), end=', ')
print("89")
