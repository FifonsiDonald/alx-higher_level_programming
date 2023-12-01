#!/usr/bin/python3
 __name__ == '__main__':
    import sys
    if len(sys.argv) - 1 == 1:
    print("{} argument:".format(len(sys.argv) - 1))
    elif len(sys.argv) - 1 == 0:
    print("{} arguments.".format('0'))
    else:
    print("{} arguments.".format(len(sys.argv) - 1))
    for i in range(len(sys.argv) - 1):
    print("{}: {}".format(i + 1, sys.argv[i + 1]))
