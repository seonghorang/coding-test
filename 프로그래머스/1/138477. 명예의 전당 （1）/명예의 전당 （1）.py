def solution(k, score):
    scores = []
    answer = []
    for s in score:
        if len(scores)+1 <= k:
            scores.append(s)
            answer.append(sorted(scores)[0])
        else:
            scores.sort()
            if sorted(scores)[0] < s:
                scores[0] = s
                answer.append(sorted(scores)[0])
            else:
                answer.append(scores[0])
    return answer