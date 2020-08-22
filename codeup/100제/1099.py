panel = []
for a in range(10):
    pre_panel = list(map(int,input().split()))
    panel.append(pre_panel)

x = 1
y = 1

while True:
    if panel[x][y] == 2 or (x,y) == (8,8):
        panel[x][y] = 9
        break
    panel[x][y] = 9
    y = y+1
    if panel[x][y] == 1:
        y = y-1
        x = x+1



for a in range(0, 10):
    for b in range(0, 10):
        print(str(panel[a][b])+' ',end='')
    print()