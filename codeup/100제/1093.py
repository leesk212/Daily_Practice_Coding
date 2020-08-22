len_s = int(input())
input_data = list(map(int,input().split()))

data = [
        0,0,0,0,0,0,0,0,0,0
        ,0,0,0,0,0,0,0,0,0,0
        ,0,0,0,0
        ]

for a in input_data:
    data[a] = data[a] + 1

for a in range(1, len(data)):
    print(str(data[a])+" ",end='')

