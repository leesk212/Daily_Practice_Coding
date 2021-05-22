from itertools import permutations

def solution(numbers):
    
    answer = 0
    
    permutes = permutations(numbers,len(numbers))
    print(permutes)
    for each in permutes:
        box = ''
        for idx in range(len(numbers)):
            box = box+str(numbers[each[idx]])
        pre_answer = int(box)
        if pre_answer > answer:
            answer = pre_answer
        
    return answer
