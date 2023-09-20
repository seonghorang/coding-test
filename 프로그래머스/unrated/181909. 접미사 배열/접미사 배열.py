def solution(my_string):
    answer = []
    for idx in range(0,len(my_string),1):
        answer.append(my_string[idx:])
    answer.sort()
    return answer