#!/usr/bin/python3
def uniq_add(my_list=[]):
    reduce = set(my_list)
    res = 0
    for i in reduce:
        res += i
    return res
