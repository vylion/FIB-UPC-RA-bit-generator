# Random Algorithms
## Assignment 01

This is Assignment 01 of the Random Algorithms course, from the MIRI Master degree at FIB, UPC. Autumn 2019

### BitString

This is a custom class that stores a string of bits as a string, the equivalent integer value, and a series of functions to compare between them.

Definition is as the following: `b = BitString(bits)` where `bits` is a given string of bits (used for testing purposes).

The class also has the functions `Random(length=16)`, which returns a new BitString with a string of length `length` (defaults to 16) and bits randomized one by one; and the function `dominates(self, other)` which returns `True` if `self` has `1`s on at least all positions where `other` has `1`s too, and `False` otherwise (this is implemented through bitwise AND).

### BitSet

This is a custom class that generates a random list of BitStrings, ordered by equivalent integer value.

Definition is as the following: `BitSet(size=5000, bits=16)` where `size` is the number of BitStrings (defaults to 5000), and `bits` is the number of bits in a BitString. There is no way to have non-randomized BitStrings, because that is not the purpose of this class.

This class also has a function `find_dominated()` which classifies all BitStrings into dominated (if they are dominated by at least 1 other BitString in the BitSet) or non-dominated (if they are not dominated by any other BitString in the set). Since the set is ordered, it does so by taking each BitString b, and then comparing with each other BitString b2 _starting from the end_, and stopping when b2 == b1 (since that would give a false positive; and also, a BitString cannot be dominated by any lesser number since by definition, lesser numbers have less `1`s).

**Edge case:** when a BitString is repeated. Usually, since a BitString has to be dominated by _another_ one to count, comparison with itself is avoided. However, in this case there _is_ another BitString (with the same `1`s exactly) that does dominate it. When looping, if the index of the currently evaluated BitString is reached, it also checks for the previous one in case there is another one equal to itself.

### Generator

This file has 3 functions:

- `test()`: Tests the dominance operator, by setting 2 hardcoded BitStrings and comparing them, expecting `True` to be printed out.
- `one_set():` Generates one set, to test it does so properly.
- `do_assignment(repeats=10, m=16, size=5000):` Does the assignment. This is, it generates a `repeats` number of sets of `size` BitStrings, with `m` bits each, and then finds the number of non-dominated BitStrings of each set, and the median of all those. It also appends the results to a `generated.txt` file (it creates it first if it doesn't exist).

The `main()` function currently calls `do_assignment()` for the default configuration of 10 repeats, 16 bits and 5000 BitStrings, but can be edited.
