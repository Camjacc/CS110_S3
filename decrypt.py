import rsa
import stdio
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    d = int(sys.argv[2])
    width = rsa.bitLength(n)

    message = str(stdio.readAllStrings())

    for i in range(0, len(message) - 1, width):
        s = message[i:i + width - 1]
        y = rsa.bin2dec(s)
        value = rsa.decrypt(y, n, d)
        stdio.write(chr(value))

if __name__ == "__main__":
    main()
