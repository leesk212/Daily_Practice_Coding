# Chapter3 그리디




# Chapter4 구현
## 구현
  머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정
  (어떻게 풀면 되는지 감은 오지만, 막상 코드로 옮기려니 무엇부터 작성해야 할지 모르는 경우)
  * 문법의 부족
  * 라이브러리 사용의 경험 부족
  
    ( ex: N개의 원소가 들어 있는 리스트에서 R개의 원소를 뽑아 한줄로 세우는 모든 경우(순열) -> python의 itertools의 라이브러리 사용가능 )
  
  **구현유형: 완전탐색 유형, 시뮬레이션 유형**
  * 완전탐색: 모든 경우의 수를 주저 없이 다 계산하는 해결 방법
  * 시뮬레이션: 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행
  
  메모리 관련 문제에서 python이 가장 접근하기가 쉽지만 느리다. 하지만 pypy3의 환경에서는 충분히 C와 C++ 만큼 빠르다.
  또한 웹이나 api개발, 데이터 분석 부분에서 python을 따라올 수 없다.
  
  1. 예제 4-1 상하좌우 (1_simulation_상하좌우.py)
  <pre>
  <code>
#My_code
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
</code></pre>  
  
<pre><code>
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


</code></pre>  

   문제 해설 코드의 방향으로 효율적으로 코딩을 진행해보자 