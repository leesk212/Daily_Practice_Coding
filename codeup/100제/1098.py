def reverse_num(a):
    if a == 1:
        return 0
    if a == 0:
        return 1

panel_x,panel_y = map(int,input().split())
panel = []
for a in range(panel_x):
    pre_panel=[]
    for b in range(panel_y):
        pre_panel.append(0)
    panel.append(pre_panel)

count = int(input())
for a in range(count):
    l,d,x,y = map(int,input().split())
    x = x-1
    y = y-1

    if d == 0:    #왼쪽
        for b in range(l):
            panel[x][y+b] = reverse_num(panel[x][y+b])
    if d == 1:    #위쪽
        for b in range(l):
            panel[x+b][y] = reverse_num(panel[x+b][y])

for a in range(0, panel_x):
    for b in range(0, panel_y):
        print(str(panel[a][b])+' ',end='')
    print()