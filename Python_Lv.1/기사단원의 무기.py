# include <stdio.h>
# include <stdbool.h>
# include <stdlib.h>
def get_divider_cnt(number):
    d = []

    for i in range(1, int(number ** 0.5 + 1)):
        if number % i == 0:
            d.append(i)
            if i != number//i:
                d.append(number//i)
    return len(d)


def solution(number, limit, power):
    answer = 0
    iron_weight = 0

    for i in range(1, number+1):
        curr_divider = get_divider_cnt(i)
        if curr_divider > limit:
            iron_weight = power
        else:
            iron_weight = curr_divider
        answer += iron_weight
    return answer


print(solution(5, 3, 2))  # 10
print(solution(10, 3, 2))  # 21
