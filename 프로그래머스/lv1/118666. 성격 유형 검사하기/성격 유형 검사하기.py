def solution(survey, choices):
    kko_score = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    cho_score = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    answer = ''
    for kko_type, cho in zip(survey, choices):
            if cho < 4:
                kko_score[kko_type[0]] +=cho_score[cho]
            elif cho >= 5:
                kko_score[kko_type[1]] +=cho_score[cho]
    
    kko_keys = list(kko_score.keys())
    
    for left,right in zip(kko_keys[::2],kko_keys[1::2]):
        if kko_score[left] >= kko_score[right]:
            answer += left
        else:
            answer += right
    return answer