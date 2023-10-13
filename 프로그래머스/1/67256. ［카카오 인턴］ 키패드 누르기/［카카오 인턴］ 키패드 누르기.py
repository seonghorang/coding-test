def solution(numbers, hand):
    keypad = {1:(0,0), 2:(0,1), 3:(0,2),
              4:(1,0), 5:(1,1), 6:(1,2),
              7:(2,0), 8:(2 ,1) ,9: (2 ,2),
              '*':(3 ,0) , 0:(3 ,1) ,'#':(3 ,2)}
    
    location_left = '*' 
    location_right = '#' 
    answer = ''
    for number in numbers:
        if number in [1 ,4 ,7]:
            answer += 'L'
            location_left = number
        elif number in [3 ,6 ,9]:
            answer += 'R'
            location_right = number
        else:
            curPos = keypad[number]
            
            leftDist= abs(keypad[location_left][0] - curPos[0]) + abs(keypad[location_left][1] - curPos[1])
            
            rightDist= abs(keypad[location_right][0] - curPos[0]) + abs(keypad[location_right][1] - curPos[1])
            
            if leftDist > rightDist:
                answer += 'R'
                location_right = number
            elif leftDist < rightDist:
                answer += 'L'
                location_left = number
            else:
                if hand == "right":
                    answer += 'R'
                    location_right = number
                else:
                    answer += 'L'
                    location_left = number
                    
    return answer
