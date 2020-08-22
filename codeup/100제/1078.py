data = int(input())
temp = int()
for i in range(1,data+1):
    if i % 2 == 0:
        temp = temp + i
print(temp)