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
ans = 0
n_a = int()
n_b = int()
while True:
    for i in range(4):
        n_a = a + move_x[i]
        n_b = b + move_y[i]
        if MAP[n_a][n_b] == 1 or MAP[n_a][n_b]:
            count += 1
    if count == 4:
        print(ans)
        break

    MAP[a][b] = 9
    index = index + 1
    if index == 4:
        index = 0
    d = direction[index]
    for i in range(len(direction)):
        if d == direction[i]:
            n_a = a + move_x[i]
            n_b = b + move_y[i]

    if MAP[a][b] != 0:
        continue

    a = n_a
    b = n_b

    ans += 1
