def solution(nums):
    ### 각 번호별 빈도수 체크를 위한 딕셔너리
    cnt={}
    ### 딕셔너리에 번호가 있으면 그 번호 빈도수 1증가
    ### 없으면 번호 추가하고 빈도수 1
    for n in nums:
        if n in cnt:
            cnt[n] += 1
        else:
            cnt[n] = 1
    ### n/2와 종류갯수 계산
    answer = min(len(nums)//2,len(cnt))
    return answer