first,second = map(str, input().split())
if first[0] == '-':
    F = int(first[1:])*-1
else:
    F = int(first)

if second[0] == '-':
    S = int(second[1:])*-1
else:
    S = int(second)

print(F+S)