#My code
N = int(input())
data = []
count = 0
for n in range(N+1):
    for m in range(0,60):
        for s in range(0,60):
            data = str(n) + str(m) + str(s)
            for index in range(len(data)):
                if data[index] == '3':
                    count = count + 1
                    break
print(count)

#문제 해설 code
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k): #if문안에서 바로 검색 하는 것이 더욱 효율적이다.
                 count += 1

print(count)