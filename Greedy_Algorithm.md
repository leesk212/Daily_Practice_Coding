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

# Properites of Greedy Algorithm
 * 최적화 문제가 있는데 그르디 알고리즘이 이것을 해결하는 것을 우리가 어떻게 알 수 있는가?
 * 항상 동작하는 방법은 없지만, Greedy-choice property를 표시할 때 최적 부분구조를 같기 때문에 뒤에 property를 야기하는 상황에서 자주 그렇게 한다. two key ingredients 

# Greedy choice property
* 부분적으로 최적의 해를 선택함으로써 전체적으로 최적의 해를 만든다. greedy라는 것은 욕심쟁이 선택이 될 뿐만아니라, 부분적으로 최적의 선택일때 최선의 선택을 할때 그 순간에 베스트하게 보이는 선택들을 한다.
* 다른말로 우리가 어떤 선택을 할지 고려할 때 가장 최적의 선택을 고려하는데 **모든 부분문제들에 대한 결과들을 모르는 상황에서 best로 보이는 것을 선택한다** 계속적으로 이를 수행할 결과, 부분문제들이 계속 size가 줄어들게 되면서 최종적으로 전체를 다 이루게 되는 형태이다.

# Dynamic Programming vs Greedy
* Greedy Choice(Locality Optimal 한것을 모두 선택하였더니 부분문제들이 줄어들며 이것들이 모여 최종적으로 Global한 해가 된다)와 Optimal-Substructure 을 만족하면 Greedy Algorithm
* Optimal - Substructure은 최적은 부분 성질을 만족하는 것이다.
* Greedy -> Top down
* Greedy에서는 어떤 것을 선택을 하던 그 상황에서만 가장 최고인 것을 선택한다. (다른 것들을 신경 쓰지 않고!!!)
* Greedy Algorithm에서 만든 선택들에는 다른 것에는 선택을 받을지 모를 지라도, 미래에 일어날 선택들에 종속 될 수 없고, 
* DP는 부분문제들을 푸는데, 첫번째 문제를 풀기 전에 subp problem을 먼저 푼다. 

# 0-1 vs Fractional
* 0-1 : Greedy Property 만족 x
* Fractional : Greedy Property 만족

# Dynamic Porgramming
* 부분문제들의 해들을 만족한다.
* 하지만 Subproblem들의 해들의 선톡 의존(종속이 된다.)한다. (Greedy Algorithm과 차이점)
* DP를 해결할때 대부분 bottump up을 사용하는데, 이렇게 하는 것은 결국, Subproblem들을 알아야 더 큰 부분문제들을 해결하는 것이기에
* Bottom up 대신에 Top Down으로도 풀 수 있는데 memorization을 통해 풀 수도 있다.
* 부분 문제들을 풀어야만 한다. 

# Greedy Choice를 더욱 효율적으로 하는 법
* 전처리를 하거나, 또는 Priority Queue를 사용함 (다이스트라 or 밸만코드)


# Optimal - Substructure Property
* optimal substructure은 부분들의 해들이 최적의 해를 보여주고 있으면 optimal substructure이 된다고 볼 수 있다.
* 부분문제에 대한 Greedy한 선택과 결합이 되어서 적절한 해가 산출되는 것이 필요하다.
* 원래문제의 최적의해가 부분문제의 최적의 해를 포함 하고 있으면 된다.  
* implicitly 하게 문제를 해결 하는 것이다. 어떤거의 greedy라면 부분문제들의 수학적 귀납법을 해결하는 것이다.



# 0-1 knapsack problem
* 배낭문제
* 배낭문제 유형중에 0-1이다. 
* 도둑이 가게의 물건을 훔치려는데 n개의 item들이 있다. 이때 i번째 물건의 값어치는 vi이다. 그리고 이것의 무게는 wi이다.  
* 배낭에 최대한 비싼 물건들을 담아 두는 것이다. 그러나 최대한 많아야하며 그의 배낭에 Wpound만큼만 담을 수 있으며 Maximum weight이다. (이때 이것은 integer이고 이때 얼마나의 무게를 취득해야만 하는가?)
* 0-1문제라고 불리는 이유는 "그물건에 대해서 갖거나 안갖거나 이분법으로 나타낼 수 있기 때문이다" 2진결정!!
* item의 부분적인 양을 갖고갈 수 없다. 아이템을 조개서 가져갈 수 있으면 Fractional이 된다.!! 
* 아이템을 1번이상을 가져가는 것은 할 수 없다. 
* 여러개를 고려하고 싶으면 index 는 1~5까지 동일하게 두면 된다. 
