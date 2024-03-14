#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the sum of arguments"""
    import sys

    sum_arguments = 0
    for i in range(len(sys.argv) - 1):
        sum_arguments += int(sys.argv[i + 1])
        if (i != 0):
            print("{}".format(sum_arguments))
        else:
            print("0")
