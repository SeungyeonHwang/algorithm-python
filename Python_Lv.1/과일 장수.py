def solution(k, m, score):
    answer = 0
    score.sort()
    size = len(score)
    fruit_divide = size % m

    for i in range(fruit_divide, size, m):
        print(fruit_divide)
        print(score[i] * m)
        answer += score[i] * m

    return answer


print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
