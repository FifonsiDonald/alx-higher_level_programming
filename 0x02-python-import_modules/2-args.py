#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    arlen = len(sys.argv) - 1
    if (arlen) == 1:
        print("{} argument:".format(arlen))
    elif arlen == 0:
        print("{} arguments.".format('0'))
    else:
        print("{} arguments.".format(arlen))
    for i in range(arlen):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
