import random


class BitString:
    def __init__(self, bits=''):
        self.s = bits
        self.n = int(self.s, 2)

    def Random(length=16):
        s = ''
        for _ in range(length):
            s += '1' if random.getrandbits(1) else '0'
        return BitString(s)

    def dominates(self, other):
        return (self.n & other.n) == other.n

    def __lt__(self, other):
        return self.n < other.n

    def __le__(self, other):
        return self.n <= other.n

    def __eq__(self, other):
        return self.n == other.n

    def __gt__(self, other):
        return self.n > other.n

    def __ge__(self, other):
        return self.n >= other.n

    def __ne__(self, other):
        return self.n != other.n

    def __str__(self):
        return self.s

    def __repr__(self):
        return self.s
