import math
import stdio
import sys


# Entry point (DO NOT EDIT).
def main():
    n = int(sys.argv[1])
    x, y = [], []
    for i in range(n):
        x += [stdio.readFloat()]
    for i in range(n):
        y += [stdio.readFloat()]
    stdio.writeln(_distance(x, y))


def _distance(x, y):
    n = len(x)
    d = 0.0

    for i in range(n):
        d += (x[i] - y[i])**2
    return math.sqrt(d)


if __name__ == "__main__":
    main()
