whitelists = list(set([tuple(set(whitelist)) for whitelist in whitelists]))

# [ 
#   [1,q]
#   [2,s]
#   [3,4]
#   [1,q]
# ]
# 이라면 저 문법 후 [[1,q],[2,s],[3,4]]가 된다. 하지만 각 원소의 값은 랜덤으로 바뀌게 된다.
