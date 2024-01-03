#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        cap = 0
    else:
        cap = 32
    print("{:c}".format(i - cap), end='')
