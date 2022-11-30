"""
빈병 2 -> 콜라 1병
빈병 20 -> 콜라 ? 병
빈병 2 미만 -> X
a : 빈병 갯수
b : 콜라 갯수
n : 보유 빈병
result : 콜라 획득 갯수
"""


def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += (n // a) * b
        n = (n // a) * b + (n % a)
        print(n)
    return answer


solution(2, 1, 20)
