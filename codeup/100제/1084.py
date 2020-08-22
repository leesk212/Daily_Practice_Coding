data = list(map(int,input().split()))
count = int()
for f in range(data[0]):
    for s in range(data[1]):
        for t in range(data[2]):
            print(str(f)
                  +" "
                  +str(s)
                  +" "
                  +str(t)
            )
            count = count+1
print(count)