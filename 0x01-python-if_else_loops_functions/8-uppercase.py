#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            cap = 32
        else:
            cap = 0
        print("{:c}".format(ord(str[i]) - cap), end='')
    print()

uppercase("Best School 98 Battery street")
