def solution(food):
    answer=''
    for i in range(1,len(food)):
        answer += f'{i}'*(food[i]//2)
    values = list(reversed(answer))
    answer += '0'
    for value in values:
        answer += value
    return answer