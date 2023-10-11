def solution(array, commands):
    answer = []
    for value in commands:
        i = value[0]
        j = value[1]
        k = value[-1]
        answer.append(sorted(array[i-1:j])[k-1])
    return answer