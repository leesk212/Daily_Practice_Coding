data = list(map(int,input().split()))

for a in data:
    if a < 0:
        print('minus')
    else:
        print('plus')
    if a % 2 == 0:
        print('even')
    if a % 2 == 1:
        print('odd')