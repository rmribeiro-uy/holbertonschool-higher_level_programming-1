#!/usr/bin/python3
if __name__ == "__main__":
    import sys
if (len(sys.argv)) < 2:
    print("0 arguments.")
else:
    if (len(sys.argv)) == 2:
        print("{:d} argument:".format((len(sys.argv)) - 1))
    else:
        print("{:d} arguments:".format((len(sys.argv)) - 1))
    for string in range(1, (len(sys.argv))):
        print("{:d}: {}".format(string, sys.argv[string]))
