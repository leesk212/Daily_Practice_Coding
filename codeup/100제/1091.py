a, m, d, n = map(int, input().split())
index = 1
while True:
    if index == n:
        print(a)
        break
    a = a * m
    a = a + d
    index = index + 1


