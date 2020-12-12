# Content
* Designing Greedy Algorithm : 지역적 최선을 선택하는 알고리즘이다. (locality best)
* Properites of Greedy Algorithms (두가지를 만족할 수 있다.)
  * Greedy-Choice Property (그리디로 해서도 전체적인 최적의 해를 찾을 수 있다.)
  * Optimal-Substructure Property (Dynamic Programming이랑 닮은 것이 있다.)
* Greedy vs DP (위 2가지중 2가지다 맞으면 Greedy로 풀고, 그것이 아니라 optimal 만 맞을 경우 overlapping이 맞는지 확인후 DP로 문제를 해결한다.[부분 문제 해결][부분문제 끼리 보니까 중복이 있네!! )
* 0-1 Knapsack Problem ( 배낭에 물건을 담을지 말지)
* Fractional Knapsack Problem ( 부분으로 나눌 수 있는 물건들에 대한 배낭 문제) 
[ 쪼갤 수 있으면 0,1 아니면 부분문제 ]
[ 도둑이 어느 물건을 훔치려고 할때, 배낭에는 무한대로 물건을 담을 수 없기에 그러면 각각의 물건과 가격을 주었을 때 어떤 걸 넣어주느냐..? ] 
[ 둘중의 하나는 그리디로 쉽게 구현하고, Fractional은 Greedy choice를 만족하지만 ] [ 0-1은 Grobally optimal solution을 만족 못하기 때문에 DP로 표현을 해야만한다 ] 

# Greedy Algorithm
* 1열의 선택을 함으로써 문제의 최적의 해를 찾는다. 
* 선택을 해야할때 최선의 선택을 하는 것 -->> 이것이 결국에는 global한 선택이 되더라!
* 그리디한 전략은 항상 최적의 해를 만들어내는 것은 아니지만, 대부분 만들어낸다.
* Optimal Solution이 나오지 않으면 구하면 안된다.
* 그럼으로 greedy property가 성립할때만 greedy algorithm을 만들게 된다. 모든 문제가 그리디 알고리즘을 만족하는 것이 아니다.
* 두가지 성질이 있다.

# Designing Greedy Algorithm
* 최적화 문제가 있을 때, 아이템들을 담았을 때 총 가격의 합이 Maximiztion이 되는 것 -> Fractional 문제 
* 목적을 세우고 목적을 달성할때, 제약조건들이 필요로 한다. (배낭문제에서는 배낭의 무게가 아닐까?)
* 어떤 문제로 만들 것이냐면 하나의 부분문제 하나로 남기는 것이 첫번째 단
* 1. 선택을 하게 되면 하나의 부분문제 가 남도록 하는 것 --> Greedy Algorithm
* 2. 원래의 문제에 최적의 해가 존재하는 것을 보는 것인데, Locality optimal 하는 것이 된다면 결과적으로는 Optimal Solution이 된다. --> 이때만 성립이 되면 Locality가 안정해진다.
* 3. Step2를 보면 OptimalSubstrucuture에 문제가 되는 것을 보이게 되면, 그리디한 선택을 함으로써 부분문제 하나인데, 어떤 부분문제가 있는 것이냐면 우리가 행한 그리디한 선택을 하게 되면 original 문제가 남더라
[ 최적 부분을 입증하는 문제가 될텐데, 부분문제에 대한 최적의 해를 다 선택했을 경우 원래 문제의 최적의 해를 포함 했을 때 이다.]
