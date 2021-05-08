```python
import collections 

def solution(numbers, target):
    answer = 0
    _len = len(numbers)
    _desire = 0
    queue = collections.deque([(0,0)])
    
    while queue:
        _desire, _idx = queue.popleft()
        if _idx == _len:
            if _desire == target:
                answer += 1
        else:
            number = numbers[_idx]
            queue.append((_desire + number, _idx + 1))
            queue.append((_desire - number, _idx + 1))
    
    return answer
```


그래프화 시켜서 문제를 생각하니 접근은 되었지만, 어떻게 값을 queue에 넣고 빼면서 처리할지가 머리로 잡히지 않았다.




    
#     while True:
#         for i in range(2):
#             if i == 0: #start +a
#                 init_num = number[0]
#             else: # start -a
#                 init_num = -1 * number[0]
            
#             for j, each_number in enumerate(numbers):
#                 if j == 0:
#                     continue
                
    
    
#     if _desire == target:
#         answer += 1
