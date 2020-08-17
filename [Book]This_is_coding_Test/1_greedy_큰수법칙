n,m,k = map(int,input().split())
data = list(map(int,input().split()))
 
data.sort(reverse=True)


ans = 0
m_count = 0
index = 0

while m_count is not m:
    k_count = 0
    while k_count is not k:
        if index is not 0: 
            k_count = k-1
        ans = ans + data[index]
        k_count +=1
    index +=1

print(ans)
