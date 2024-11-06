import rsa
import stdio
import sys


# Entry point.
def main():
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])
    keys = rsa.keygen(lo, hi)
    stdio.writeln(keys)




if __name__ == "__main__":
    main()
