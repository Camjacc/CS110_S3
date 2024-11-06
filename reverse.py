import stdio


# Entry point (DO NOT EDIT).
def main():
    a = stdio.readAllStrings()
    _reverse(a)
    for v in a:
        stdio.writef("%s ", v)
    stdio.writeln()


# Reverses a in place, ie, without creating a new list.
def _reverse(a):
    for i in range(len(a)//2 + 1):
        temp = a[i]
        a[i] = a[len(a)-i-1]
        a[len(a)-i-1] = temp


if __name__ == "__main__":
    main()
