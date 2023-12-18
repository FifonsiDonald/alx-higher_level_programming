#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    div = 0
    for mem in my_list:
        average += mem[0] * mem[1]
        div += mem[1]
    return (average / div)
