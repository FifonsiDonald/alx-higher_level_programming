#!/usr/bin/python3
def no_c(my_string):
    my_string.translate(my_string.maketrans({'c':None, 'C':None}))
