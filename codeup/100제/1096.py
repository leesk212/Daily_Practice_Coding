len_s = int(input())
panel = []
for a in range(20):
    pre_panel = []
    for a in range(20):
        pre_panel.append(0)
    panel.append(pre_panel)

for a in range(len_s):
    x,y = map(int,input().split())
    panel[x][y] = 1

for a in range(1, 20):
    for b in range(1, 20):
        print(str(panel[a][b])+' ',end='')
    print()