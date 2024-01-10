#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    top, bot = 0, 0
    for i in my_list:
        top += i[0] * i[1]
        bot += i[1]
    return top / bo
