 # -*- coding: utf-8 -*-
import math
import utils


def problem_1():
    raise NotImplementedError("Problem not implemented")


def problem_2():
    raise NotImplementedError("Problem not implemented")


def problem_3():
    raise NotImplementedError("Problem not implemented")


def problem_4():
    raise NotImplementedError("Problem not implemented")


def problem_5():
    raise NotImplementedError("Problem not implemented")


def problem_6():
    raise NotImplementedError("Problem not implemented")


def problem_7():
    raise NotImplementedError("Problem not implemented")


def problem_8():
    raise NotImplementedError("Problem not implemented")


def problem_9():
    raise NotImplementedError("Problem not implemented")


def problem_10():
    raise NotImplementedError("Problem not implemented")


def problem_11():
    raise NotImplementedError("Problem not implemented")


def problem_12():
    raise NotImplementedError("Problem not implemented")


def problem_13():
    raise NotImplementedError("Problem not implemented")


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


def problem_17_aux(n):
    n_dict = {0: '',
              1: "one",
              2: "two",
              3: "three",
              4: "four",
              5: "five",
              6: "six",
              7: "seven",
              8: "eight",
              9: "nine",
              10: "ten",
              11: "eleven",
              12: "twelve",
              13: "thirteen",
              14: "fourteen",
              15: "fifteen",
              16: "sixteen",
              17: "seventeen",
              18: "eighteen",
              19: "nineteen",
              20: "twenty",
              30: "thirty",
              40: "forty",
              50: "fifty",
              60: "sixty",
              70: "seventy",
              80: "eighty",
              90: "ninety"}
    if n > 1000:
        return ValueError("should be less than 1000")

    s = str(n)
    l = len(s)

    if l == 1:
        return n_dict[n]
    elif l == 2 and n >= 20:
        if s[1] == '0':
            return n_dict[int(s[0]+'0')]
        return '%s-%s' % (n_dict[int(s[0]+'0')], n_dict[int(s[1])])
    elif l == 2 and n < 20:
        return n_dict[n]
    elif l == 3:
        if s[1] != '0' and s[2] != '0':
            if int(s[1:]) < 20:
                return '%s hundred and %s' % (n_dict[int(s[0])], n_dict[int(s[1:])])
            return '%s hundred and %s-%s' % (n_dict[int(s[0])], n_dict[int(s[1]+'0')], n_dict[int(s[2])])
        elif s[1] != '0' and s[2] == '0':
            return '%s hundred and %s' % (n_dict[int(s[0])], n_dict[int(s[1]+'0')])
        elif s[2] == '0' and s[1] == '0':
            return '%s hundred' % n_dict[int(s[0])]
        elif s[2] != '0' and s[1] == '0':
            return '%s hundred and %s' % (n_dict[int(s[0])], n_dict[int(s[2])])
        else:
            tmp = '%s hundred and %s' % (n_dict[int(s[0])], n_dict[int(s[2])])
            return tmp[:-1]
    elif n == 1000:
        return 'one thousand'


def problem_17(n=1000, white_spaces=False, separator='', hyphens=False, show_result=False):
    r = separator.join([problem_17_aux(x) for x in range(1, n+1)])
    if not white_spaces:
        r = r.replace(' ', '')
    if not hyphens:
        r = r.replace('-', '')
    return (r, len(r)) if show_result else len(r)


def problem_18(input_pyramid=''):
    input_pyramid = input_pyramid or "75\n" \
                                     "95 64\n" \
                                     "17 47 82\n" \
                                     "18 35 87 10\n" \
                                     "20 04 82 47 65\n" \
                                     "19 01 23 75 03 34\n" \
                                     "88 02 77 73 07 63 67\n" \
                                     "99 65 04 28 06 16 70 92\n" \
                                     "41 41 26 56 83 40 80 70 33\n" \
                                     "41 48 72 33 47 32 37 16 94 29\n" \
                                     "53 71 44 65 25 43 91 52 97 51 14\n" \
                                     "70 11 33 28 77 73 17 78 39 68 17 57\n" \
                                     "91 71 52 38 17 14 91 43 58 50 27 29 48\n" \
                                     "63 66 04 68 89 53 67 30 73 16 69 87 40 31\n" \
                                     "04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

    pyramid = [map(int, row.split()) for row in input_pyramid.split('\n') if row]
    while len(pyramid) > 1:
        low_row = pyramid.pop()
        top_row = pyramid.pop()
        new_row = []

        for index, value in enumerate(top_row):
            new_row.append(top_row[index] + max(low_row[index], low_row[index + 1]))
        pyramid.append(new_row)
    return pyramid[0][0]


def problem_19():
    raise NotImplementedError("Problem not implemented")


def problem_20(n=100):
    return sum(map(int, str(math.factorial(n))))


def problem_21():
    raise NotImplementedError("Problem not implemented")


def problem_22():
    import string
    alph_dict = dict([(x, i+1) for i, x in enumerate(string.ascii_uppercase)])
    result = 0
    with open('./problems_data/problem_22_names.txt') as fnames:
        names = fnames.readline()

    names = names.replace('"', '').split(',')

    for index, name in enumerate(sorted(names)):
        name_count = 0
        for c in name:
            name_count += alph_dict[c]
        result += name_count * (index + 1)

    return result


def problem_23():
    raise NotImplementedError("Problem not implemented")


def problem_25():
    raise NotImplementedError("Problem not implemented")


def problem_26():
    raise NotImplementedError("Problem not implemented")


def problem_27():
    raise NotImplementedError("Problem not implemented")

