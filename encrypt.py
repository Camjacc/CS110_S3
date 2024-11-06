import rsa
import stdio
import sys


# Entry point.
def main():
    n = int(sys.argv[1])
    e = int(sys.argv[2])
    width = int(rsa.bitLength(n))

    message = str(stdio.readAllStrings())

    for c in message:
        x = ord(c)
        letter = rsa.encrypt(x, n, e)
        stdio.write(str(rsa.dec2bin(letter, width)))

    stdio.writeln()




if __name__ == "__main__":
    main()
