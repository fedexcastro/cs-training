 # -*- coding: utf-8 -*-
import math
import utils


def problem_14(to=1000000):
    """
    Longest Collatz sequence:
    The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    """
    maximum = 0
    result = 2
    for number in xrange(2, to):
        n = number
        long_chain = 1
        while number != 1:
            if number % 2:
                number = 3*number + 1
            else:
                number /= 2
            long_chain += 1

        if maximum < long_chain:
            maximum = long_chain
            result = n

    return "The number %s produces a chain of %s" % (result, long_chain)


def problem_15():
    """
    Starting in the top left corner of a 2×2 grid, and only being able to move
    to the right and down, there are exactly 6 routes to the bottom right corner.

    How many such routes are there through a 20×20 grid?
    """

    print """
    Answer:
    The number of such paths in an m×n grid is mCn(m+n, m) = mCn(m+n, n).

    The reason is quite simple: you must make a total of m+n moves,
    consisting of m moves down and n to the right, in any order,
    and there are (m+nm) ways to choose which of the m+n moves are down
    (or, equivalently, (m+nn) ways to choose which n of them are to the right).
    """

    return utils.mCn(40, 20)


def problem_16():
    return sum(map(int, str(2**1000)))


def problem_17():
    raise NotImplementedError("Problem not implemented")


def problem_18():
    raise NotImplementedError("Problem not implemented")


def problem_19():
    raise NotImplementedError("Problem not implemented")


def problem_20():
    raise NotImplementedError("Problem not implemented")


def problem_21():
    raise NotImplementedError("Problem not implemented")


def problem_22():
    raise NotImplementedError("Problem not implemented")


def problem_23():
    raise NotImplementedError("Problem not implemented")


def problem_25():
    raise NotImplementedError("Problem not implemented")


def problem_26():
    raise NotImplementedError("Problem not implemented")


def problem_27():
    raise NotImplementedError("Problem not implemented")

