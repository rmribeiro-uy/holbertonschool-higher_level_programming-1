#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    count = len(sys.argv)
    for nums in range(1, count):
        sum = sum + int(sys.argv[nums])
    print("{}".format(sum))
