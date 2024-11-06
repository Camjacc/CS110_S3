import stdio
import stdrandom
import sys


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    primes = _primes(lo, hi)

    r1 = stdrandom.uniformInt(0, len(primes) - 1)

    p = primes[r1]

    r2 = stdrandom.uniformInt(0, len(primes) - 1)

    q = primes[r2]

    n = p * q

    m = (p - 1) * (q - 1)

    mprimes = _primes(2, m)

    e = m

    while m % e == 0:
        r = stdrandom.uniformInt(0, len(mprimes) - 1)
        e = mprimes[r]

    for d in range(1, m):
        if (d * e) % m == 1:
            break

    tuple = (n, e, d)

    return tuple

# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    encrypted = (x ** e) % n
    return encrypted


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    decrypted = (y ** d) % n
    return decrypted

# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, "0%db" % (width))


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    primes = []
    for i in range(lo, hi):
        j = 2
        while j < i:
            if i % j == 0:
                break
            else:
                j += 1
        if j == i:
            primes += [i]
    return primes


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
     b = a
     shuffled = []
     for i in range(k):
         r = stdrandom.uniformInt(0, k - 1)
         temp = b[i]
         b[i] = b[r]
         b[r] = temp
         shuffled += b[r]
     return shuffled

# Returns a random item from the list a.
def _choice(a):
    r = stdrandom.uniformInt(0, len(a) - 1)
    return a[r]



# Unit tests the library [DO NOT EDIT].
def _main():
    c = sys.argv[1]
    x = ord(c)
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef("encrypt(%c) = %d\n", c, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef("decrypt(%d) = %c\n", encrypted, chr(decrypted))
    width = bitLength(x)
    stdio.writef("bitLength(%d) = %d\n", x, width)
    xBinary = dec2bin(x, width)
    stdio.writef("dec2bin(%d) = %s\n", x, xBinary)
    stdio.writef("bin2dec(%s) = %d\n", xBinary, bin2dec(xBinary))


if __name__ == "__main__":
    _main()
