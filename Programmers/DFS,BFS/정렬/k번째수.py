def solution(array, commands):
    answer = []
    
    for command in commands:
        #print(command)
        i = command[0]
        j = command[1]
        k = command[2]
        
        if i != j:
            post_array = array[i-1:j]
            post_array = sorted(post_array)
            pre_answer = post_array[k-1]
        else:
            pre_answer = array[i-1]
            
        answer.append(pre_answer)
    
    return answer
