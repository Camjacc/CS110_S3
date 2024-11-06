import stdio
import sys


# Entry point (DO NOT EDIT).
def main():
    s = sys.argv[1]
    stdio.writeln(_isPalindrome(s))


# Returns True if s is a palindrome and False otherwise.
def _isPalindrome(s):
    n = len(s)
    for i in range(n):
        if s[i] != s[n-1-i]:
           return False
        else:
            return True



if __name__ == "__main__":
    main()
