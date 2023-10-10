def solution(price, money, count):
    p = 0
    for c in range(count+1):
        p += price*c
    if p - money <= 0:
        answer = 0
    else:
        answer = p - money
    return answer