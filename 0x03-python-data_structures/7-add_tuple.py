#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tlist =[[0, 0], [0, 0]]
    if len(tuple_a) > 0:
        tlist[0][0] = tuple_a[0]
        if len(tuple_a) > 1:
             tlist[0][1] = tuple_a[1]
    if len(tuple_b) > 0:
        tlist[1][0] = tuple_b[0]
        if len(tuple_b) > 1:
             tlist[1][1] = tuple_b[1]
    new_tuple = (tlist[0][0] + tlist[1][0]), (tlist[0][1] + tlist[1][1])
    return new_tuple
