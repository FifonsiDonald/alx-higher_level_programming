#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    division = list()
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = None
        except ZeroDivisionError:
            print("division by 0")
            div = None
        except IndexError:
            print("out of range")
            div = None
        finally:
            division.append(div)
    return division
