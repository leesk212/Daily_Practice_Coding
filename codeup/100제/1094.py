len_s = int(input())
input_data = list(map(int,input().split()))
input_data.reverse()
for a in range(len_s):
    print(str(input_data[a])+" ",end='')