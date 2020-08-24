#형태가 섞여있는 것 중에서 시간만 따로 비교하고 싶으면 다음과 같이 하면 된다.

all_indicies = sorted(all_indicies, key=lambda x: datetime.datetime.strptime(x, 'winlogbeat-%Y.%m.%d'))


# 그리고 일반적인 시간들은 그냥 비교하면 자동으로 비교가 된다.


# 시간을 pharsing 하는 과정 중 find 함수는 계속 그 위치를 갖고 있어주어야 한다.
# 시작 시간만 find의 시작점을 주었다고 해서 가능한 일이 아니다.