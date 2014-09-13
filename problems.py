from graph import bfs, dfs


def stable_colors(array):
    n = len(array)
    avg = sum(array) / 3
    if not n or n < 3 or avg % 1:
        return 'impossible'

    colored = {'R': 0, 'G': 0, 'B': 0}

    tmp = sorted(enumerate(array), key=lambda x: x[1])

    for color, s in colored.items():
        if not tmp:
            return 'impossible'
        j = 1
        index, s = tmp.pop()
        array[index] = color

        while tmp and s < avg:
            if len(tmp) < j:
                return "impossible j %s, tmp %s" % (j, tmp)
            i, v = tmp[-j]
            if v + s <= avg:
                s += v
                array[i] = color
                tmp.remove((i, v))
            else:
                j += 1

    for i, v in tmp:
        if not v:
            array[i] = 'G'  # I like green!
        else:
            break

    return ''.join(array)


def solution(tree):
    final_path, paths = dfs(tree, return_paths=True)
    result = 0
    for path in paths:
        if path:
            if max(path) == path[-1]:
                result += 1
    return result


def solution2(array):
    if not array:
        return 0
    m = 0
    n = len(array)
    visited = [False for _ in range(n)]
    results = lambda l: sum([1 for x in l if not x])
    visited[0] = True
    loop_control = []

    while True:
        m = m + array[m]
        if m >= n or m < 0:
            return results(visited)
        elif visited[m]:
            loop_control.append(m)
            if len(loop_control) > n:
                return results(visited)
        elif not visited[m]:
            loop_control = []
            visited[m] = True

    return sum([1 for x in visited if not x]), visited



A = [-1, 3, -4, 5, 1, -6, 2, 1]


def solution3(A):
    # write your code in Python 2.7
    if not A:
        return -1

    try:
        iter(A)
    except TypeError:
        return -1

    l = len(A)

    total_sum = sum(A)
    s = 0

    for index, elem in enumerate(A):
        if not isinstance(elem, int):
            return -1
        os = total_sum - s - A[index]
        if s == os:
            return index
        s += elem

    return -1


def validate_iterable(elem, elem_type=None):
    try:
        it = iter(elem)
        if elem_type:
            for e in it:
                if not isinstance(e, elem_type):
                    raise ValueError
    except (TypeError, ValueError):
        return ValueError("Invalid input")


def validate_integer(elem, min, max):
    if not (isinstance(elem, int) and min <= elem <= max):
        raise ValueError("Element is not a valid integer")


def toptal1(X, A):
    validate_integer(X, 0, 100000)
    validate_iterable(A, elem_type=int)
    l = len(A)

    def P(T):
        validate_integer(l, 0, l)
        return sum([1 for e in range(0, T) if A[e] == X])

    def Q(T):
        validate_integer(l, 0, l)
        return sum([1 for e in range(0, T) if A[e] != X])

    for index in range(1, l):
        if Q(index) == P(index):
            return index
    return -1


def toptal2(M):
    # write your code in Python 2.7
    digits = []
    if not M:
        digits = [0]
    else:
        while M != 0:
            M, remainder = divmod(M, -2)
            if remainder < 0:
                M, remainder = M + 1, remainder + 2
            digits.append(remainder)
    digits = digits[::-1]
    digits.reverse()
    return digits


def toptal3(A):
    validate_iterable(A, elem_type=int)
    if not A:
        return 0
    m = sum(A)
    paths = [[False for _ in range(m)] for _ in range(m)]

    moves = ['north', 'east', 'south', 'west']
    next_move, last_x, last_y = 0, m/2, m/2

    for step, value in A:
        if next_move > 3:
            next_move = 0

        move_to = moves[next_move]

        move_n = range(1, value+1)

        if move_to == 'north':
            for s in move_n:
                last_y -= s
                if paths[last_x][last_y]:
                    return step
                paths[last_x][last_y] = True

        elif move_to == 'east':
            for s in move_n:
                last_x += s
                if paths[last_x][last_y]:
                    return step
                paths[last_x][last_y] = True

        elif move_to == 'south':
            for s in move_n:
                last_y += s
                if paths[last_x][last_y]:
                    return step
                paths[last_x][last_y] = True

        elif move_to == 'west':
            for s in move_n:
                last_x -= s
                if paths[last_x][last_y]:
                    return step
                paths[last_x][last_y] = True
        next_move += 1
    return 0


def num_bin(N, places=8):
    def bit_at_p(N, p):
        ''' find the bit at place p for number n '''
        two_p = 1 << p   # 2 ^ p, using bitshift, will have exactly one
                         # bit set, at place p
        x = N & two_p    # binary composition, will be one where *both* numbers
                         # have a 1 at that bit.  this can only happen
                         # at position p.  will yield  two_p if  N has a 1 at
                         # bit p
        return int(x > 0)

    bits =  ( bit_at_p(N,x) for x in xrange(places))
    return "".join( (str(x) for x in bits) )



def validate_iterable(elem, elem_type=None):
    try:
        it = iter(elem)
        if elem_type:
            for e in it:
                if not isinstance(e, elem_type):
                    raise ValueError
    except (TypeError, ValueError):
        return ValueError("Invalid input")


def solution_3(A):
    validate_iterable(A, elem_type=int)

    if not A:
        return 0

    m = sum(A)
    paths = [[False for _ in range(m)] for _ in range(m)]

    moves = ['north', 'east', 'south', 'west']
    next_move, last_x, last_y = 0, m/2, m/2

    for step, value in enumerate(A):
        if next_move > 3:
            next_move = 0

        move_to = moves[next_move]

        move_n = range(1, value+1)

        for s in move_n:
            if move_to == 'north':
                last_y -= s
            elif move_to == 'east':
                last_x += s
            elif move_to == 'south':
                last_y += s
            elif move_to == 'west':
                last_x -= s

            if paths[last_x][last_y]:
                return step

            paths[last_x][last_y] = True
        next_move += 1
    return 0