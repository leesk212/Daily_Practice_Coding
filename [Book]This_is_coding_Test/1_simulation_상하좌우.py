size = int(input())
data = list(map(str,input().split()))
(x,y) = (0,0)
for a in data:
    if a == 'R':
        y = y + 1
    if a == 'L':
        y = y - 1
    if a == 'U':
        x = x - 1
    if a == 'D':
        x = x + 1

    if x > size-1 or x < 0 or y > size-1 or y < 0:
        if a == 'R':
            y = y - 1
        if a == 'L':
            y = y + 1
        if a == 'U':
            x = x + 1
        if a == 'D':
            x = x - 1

print(str(x+1)+" "+str(y+1))

#문제 해설_code
n = int(input())
x,y = 1,1 #중괄호 생략 가능
plans = input().split() #어차피 str 이니까 mapping 안해도 가능

dx = [0,0,-1,1]
dy = [-1,1,0,0]
#이동 상태를 다음과 같이 지정해줌
move_types = ['L','R','U','D']

for plan in plans:
    for i  in range(len(move_types)): #훨씬 더 알고리즘 적이다.
        if plan == move_types[i]:     #dx 와 move_type의 index를 맞추어 해당 명령일 때 좌표의 이동을 인식 시켜준다.
            nx = x + dx[i]
            ny = y + dy[i]
        if nx <1 or ny < 1 or nx > n or ny > n: #범위를 넘을 경우 다음 좌표의 이동을 업데이트를 안해주면 가능하다.
            continue
        x,y = nx,ny #좌표 업데이트

print(x,y)

