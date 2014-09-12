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
