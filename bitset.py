import bisect
from bitstring import BitString


class BitSet:
    def __init__(self, size=5000, bits=16):
        self.all = []
        self.dom = []
        self.no_dom = []

        for _ in range(size):
            b = BitString.Random()
            # Ordered insert at the left of any possible repeats:
            bisect.insort_left(self.all, b)

    def find_dominated(self):
        for i in range(len(self.all)):
            b = self.all[i]
            dominated = False
            # since range start is inclusive and stop is exclusive:
            for j in range(len(self.all)-1, -1, -1):
                if i == j:
                    if j > 0 and self.all[j-1] == b:
                        self.dom.append(b)
                        dominated = True
                    break
                if self.all[j].dominates(b):
                    self.dom.append(b)
                    dominated = True
                    break
            if not dominated:
                self.no_dom.append(b)

    def __str__(self):
        o = ""
        if self.dom or self.no_dom:
            o = "\nBitSet dominated: {}".format(len(self.dom))
            o += "\nBitSet non-dominated: {}".format(len(self.no_dom))
        return "BitSet: " + str(self.all) + o
