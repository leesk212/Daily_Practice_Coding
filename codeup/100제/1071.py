data = list(map(int,input().split()))


for a in range(len(data)):
    if data[a] == 0:
        break
    print(data[a])