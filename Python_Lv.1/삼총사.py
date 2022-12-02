from itertools import combinations


def solution(number):
    return list(map(sum, list(combinations(number, 3)))).count(0)


print(solution([-2, 3, 0, 2, -5]))
