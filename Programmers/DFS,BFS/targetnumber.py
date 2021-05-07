import collections


def solution(numbers, target):
    answer = 0
    stack = collections.deque([(0, 0)])
    while stack:
        current_sum, num_idx = stack.popleft()

        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            stack.append((current_sum + number, num_idx + 1))
            stack.append((current_sum - number, num_idx + 1))

    return answer
# import collections

# def solution(numbers, target):
#     answer = 0
#     queue = collections.deque([(0,0)])
#     while queue:
#         _sum, _idx = queue.popleft()

#         if _idx == len(numbers):
#             if _sum == target:
#                 answer += 1
#         else:
#             number = numbers[_idx]
#             queue.append((_sum+number,_idx+1))
#             queue.append((_sum-number,_idx-1))

#     return answer