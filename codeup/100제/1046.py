data = list(map(int,input().split()))

print(sum(data))
print('%.1f' %(sum(data,0.0)/len(data)))