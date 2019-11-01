from statistics import median
from bitset import BitSet
from bitstring import BitString


def test():
    b = BitString('0010')
    b2 = BitString('1110')
    print(b2.dominates(b))


def one_set():
    bset = BitSet()
    bset.find_dominated()
    print(str(bset))


def do_assignment(repeats=10, size=5000, m=16):
    med = 0
    maximals = []
    print("Number of non-dominated BitStrings: ")
    for _ in range(repeats):
        bset = BitSet(size, m)
        bset.find_dominated()
        maximal = len(bset.no_dom)
        maximals.append(maximal)
        print(maximal, sep=' ', end=' ', flush=True)
    print()
    med = median(maximals)
    print("Approximation of E[M_n]: ", med)

    results = "Bits in a string: {}\nSet size: {}\nNumber of sets: {}\nApproximation of E[M_n]: {}\n----\n"

    with open("generated.txt", "a+") as file:
        file.write(results.format(m, size, repeats, med))


def main():
    do_assignment()


if __name__ == "__main__":
    main()
