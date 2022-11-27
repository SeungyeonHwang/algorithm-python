def solution(food):
    food_str = ""
    for i in range(len(food)):
        food_str += str(i) * int(food[i] // 2)
    food_str += "0"
    return food_str + food_str[0:-1][::-1]


print(solution([1, 7, 1, 2]))
