size_x, size_y = map(int, input().split())
a, b, d = map(int, input().split())

direction = ['0', '3', '2', '1']
move_x = [0, -1, 0, 1]
move_y = [-1, 0, 1, 0]

MAP = []

for i in range(size_x):
    temp = list(map(int, input().split()))
    MAP.append(temp)

index = 0
count = 0
stop = 0
n_a = 0
n_b = 0

while True:
    n_a = a + move_y[index]
    n_b = b + move_x[index]

    if MAP[n_a][n_b] == 0:
        stop = 0
        MAP[n_a][n_b] = 9  # 가본칸
        count = count + 1
        a = n_a
        b = n_b
    else:
        index = index + 1 # 방향
        stop = stop + 1
        if stop == 4:
            print(count)
            break
