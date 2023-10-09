def solution(answers):
    score_dict = {1:0,2:0,3:0}
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i] == a[i % len(a)]:
            score_dict[1] += 1
        if answers[i] == b[i % len(b)]:
            score_dict[2] += 1
        if answers[i] == c[i % len(c)]:
            score_dict[3] += 1
            
    max_score = max(score_dict.values())

    answer = [k for k,v in score_dict.items() if v == max_score]
    
    return answer