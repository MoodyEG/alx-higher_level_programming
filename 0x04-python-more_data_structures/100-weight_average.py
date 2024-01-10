#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    top, bot = 0, 0
    for i, j in my_list:
        top += i * j
        bot += i
    return top / bot
