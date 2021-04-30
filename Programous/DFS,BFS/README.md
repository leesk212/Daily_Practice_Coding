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
### **인접행렬** 저장 방식
* idea:
  * 2차원 list
  * ```python INF=99999 graph=[[0,7,5][7,0,INF][5,INF,0]]```
