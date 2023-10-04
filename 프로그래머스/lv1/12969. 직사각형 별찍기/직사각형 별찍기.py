a, b = map(int, input().strip().split(' '))
### 세로길이
for r in range(b):
    v = ''
    ### 전체길이
    for c in range(a+b):
        ### 입력받은 가로 길이만큼 * 그리기
        if c < a:
            v += '*'
        else:
            v += ''
    print(v)