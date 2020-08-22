data = int(input())
index = 0
temp = 0
while True:
    temp = temp + index
    if data <= temp:
        print(index)
        break
    index = index + 1