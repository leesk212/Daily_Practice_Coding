size_x, size_y = map(int, input().split())
a,b,d = map(int,input().split())

direction = ['0','3','2','1']
move_x = [0,-1,0,1]
move_y = [-1,0,1,0]

MAP = []

for i in range(size_x):
    temp = list(map(int, input().split()))
    MAP.append(temp)

index = 0
n_a = int()
n_b = int()
while True:
    MAP[a][b] = 9
    index = index + 1
    d = direction[index]
    for i in range(len(direction)):
        if d == direction[i]:
            n_a = a + move_x[i]
            n_b = b + move_y[i]

    if MAP[a][b] != 0:
       continue

    a = n_a
    b = n_b
