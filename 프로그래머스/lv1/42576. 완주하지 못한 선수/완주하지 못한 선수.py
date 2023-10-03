def solution(participant, completion):
    ### 이름 및 빈도수 체크
    p_cnt = {}
    c_cnt = {}
    for name in participant:
        p_cnt[name] = p_cnt.get(name,0) + 1
    for name in completion:
        c_cnt[name] = c_cnt.get(name,0) + 1
    ### 참여했지만 완주 못한 선수 이름 추출하기
    names=[]
    for name,cnt in p_cnt.items():
        ### 완주 명단에 없거나 완주 명단보다 빈도가 많은 이름(동명이인 체크)
        if name not in c_cnt or c_cnt[name] < cnt:
            names.append(name)
    ### 이름 출력
    for name in names:
        answer = name
    return answer