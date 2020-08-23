N, M = map(int, input().split())
data = []
for n in range(N):
    data.append(list(map(int, input().split())))

for n in range(N):
    data[n].sort()
max = 0
for n in range(N):
    if max < data[n][0]:
        max = data[n][0]


print(max)
