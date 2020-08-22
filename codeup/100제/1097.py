def reverse_num(a):
    if a == 1:
        return 0
    if a == 0:
        return 1

panel = []
for a in range(19):
    pre_panel = list(map(int,input().split()))
    panel.append(pre_panel)

count = int(input())

for index in range(count):
    x,y = map(int,input().split())
    for a in range(19):
        panel[x-1][a] = reverse_num(panel[x-1][a])
        panel[a][y-1] = reverse_num(panel[a][y-1])


for a in range(0, 19):
    for b in range(0, 19):
        print(str(panel[a][b])+' ',end='')
    print()

