def solution(k, score):
    answer = []
    tmp = []

    for i in score:
        tmp.append(i)
        tmp.sort(reverse=True)
        if len(tmp) > k:
            del tmp[-1]
        answer.append(min(tmp))

    return answer


print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
