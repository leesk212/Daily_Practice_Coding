# Chapter3 그리디




# Chapter4 구현
## 아이디어를 코드로 바꾸는 구현
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
  
##### 예제 4-1 상하좌우 (1_simulation_상하좌우.py)
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
   특히 탐색 및 길찾기 문제에서는 dx dy 와 nx ny의 형태로 접근하는 것이 효율적이다.
   
##### 예제 4-2 시각 (1_bruteforce_시각.py)
   <pre><code>
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
   </code></pre>
   
   <pre>
   <code>
#문제 해설 code
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k): #if문안에서 바로 검색 하는 것이 더욱 효율적이다. 
                 count += 1
                
print(count)   
   
   
   </code>
   </pre>
   
    모든 경우의 수를 탐색하는 경우가 있다면 탐색해야할 데이터의 갯수를 확인하자 
   
   다음 문제와 같이 탐색하는 최대의 갯수가 24 X 60 X 60 즉 100만을 넘지 않는다. 
   
   만약 데이터의 갯수가 100만개 이하 일때는 bruteforce를 이용해 구현하자 
   
   또한 bruteforce문제는 **시간제한** 을 확인하자 2020년 기준으로 파이썬 3.7은 1초에 2000만번의 연산까지 진행할 수 있다.
   
   그럼으로 만약 시간제한이 1초이고 데이터의 개수가 100만개의 문제가 있다면 O(NlogN) 이내의 알고리즘을 이용하여 문제를 풀어야만 한다.
   
   ( N=1,000,000일 때 Nlog2N은 약 2천만 이기 떄문이다.) 
   
## 왕실의 나이트 (1_simulation_왕실의나이트.py)
   
   <pre><code>
   #My_code
data = input()

d_c = [1,1,-1,-1,2,-2,2,-2]
d_r = [2,-2,2,-2,1,1,-1,-1]
#행,열
col, row = int(data[1]), int(ord(data[0]))-int(ord('a'))+1

count = 0

for search in range(8):
    n_c = col + d_c[search]
    n_r = row + d_r[search]
    if n_c >= 1 and n_c <= 8 and n_r >=1  and n_r <= 8:
        count += 1

print(count)


#문제 해설:
#d_c와 d_r이 tuple로 묶고 그 index를 for문에서 찾아준 후 그 위치를 다시 step[0] 과 step[1]로 접근 하였다. 
    steps = [
                (1,2),(-1,2) ...
            ]
    for step in steps:
        d_c = c + step[0]
        ...  
              
    </code>
    </pre>
   
   * 매번 panel 문제가 나올 떄 마다 헷갈리는 것이 index의 순서이다.
   
        배열은 모두 0,0부터 index가 시작한다.
   
        하지만 문제들은 대부분 a1, c2, 11 등과 같이 첫번째 시작점을 1,1로 표현한다. 
   
        (code up 에서도 이것 때문에 몇문제 헷갈렸다.)
   
        정리를 하자면 이번 문제 같은 경우 panel이 있지만 내가 배열판을 생성하지 않았기에 헷갈릴 필요없이 처음 시작점을 그대로 1,1과 같이 진행하면 된다.
   
   * col과 row의 형식과 x,y의 형식 그리고 배열에서의 a[x][y]의 형식을 혼동하지 말자 
   
        col은 colum이며 행이다. 행이란 뜻은 가로줄이란 뜻이며 다음 행의 뜻은 다음 가로줄의 의미이다.
   
        row는 row이며 열이다. 열이란 뜻은 세로줄이란 뜻이며 다음 열의 뜻은 다음 세로줄의 의미이다.
    
   * index로 생각을 해보자. 
   
        index에서 a[1][2] -> a[2][2]가 되었다는 뜻은 행이 증가한 것이고 col이 증가한 것이다.
   
        index에서 a[1][1] -> a[1][2]가 되었다는 뜻은 열이 증가한 것이고 row가 증가한 것이다.
   
   * 문제에서의 a1 
    
        문제에서 일부로 헷갈리게 a1이라는 말을 주고, a가 열 1이 행으로 주었다. 간단히 1a로 생각하고 문제를 풀어보자 
   
   * **좌표를 생각할때 기준점**
  
        매번 헷갈리지말고 실제 좌표계라는 생각을 버리고 단지 배열으로써 기준점을 잡고 생각하자
  
        c2라면 data[2][3]이다. 쓸데없이 좌표를 끌어오지말고 이러면 col은 2이고 row 는 3이다.
  
    

## 게임 개발 (1_bruteforce_게임개발.py)