# 기본 필요 지식
* Data Structure
  * stack: list 
  * queue: deque
* Recursive function
```python
def recursive_function():
  recursive_function()
  
recursive_function()
```

# DFS/BFS
## DFS
* Depth-First Search
* 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘 
* 그래프: 노드(Node) 와 간선(Edge)로 표현되며 노드를 정점(Vertex)라고 칭함.
* 두 노드가 연결되어 있는 것을 adjacency 라고 하고, 이를 표현하는 방법에 따라 **인접행렬** 및 **인접 리스트** 라고 칭한다.
* 특정한 경로로 탐색하다가 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문 후 다시 되돌아간다.
* 일반적으로 인접한 노드 중 방문하지 않은 노드가 있다면 번호가 낮은 순서부터 처리한다.
### **인접 행렬** 저장 방식
* idea:
  * 2차원 list
  ```python INF=99999 
  graph=[[0,7,5][7,0,INF][5,INF,0]]
  ```
* 직관적
### **인접 리스트** 저장 방식
* idea:
  * 하나의 list
  ```python
  graph = [ [] for _ in range(3)]
  graph[0].append( (1,7) )
  graph[0].append( (2,5) )
  graph[1].append( (0,7) )
  graph[2].append( (0,5) )
  ```
* 필요한 정보만 저장하기 때문에 메모리 효율적 사용 가능
* 하지만 인접 정보에 대한 데이터 확인이 느리다.
### Example Code
```python
def dfs(graph, v, visited):
   visited[v] = True
   print(v, end=' ')
   for i in graph[v]:
      if not visited[i]:
         dfs(graph, i, visited)
         
graph = [ [], [2,3,8], [1,7], [1,4,5], [3,5], [3,4], [7], [2,6,8], [1,7] ] 
visited = [False] * 9
dfs(graph,1,visited)
```
