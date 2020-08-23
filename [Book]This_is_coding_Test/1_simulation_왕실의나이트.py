#My_code
data = input()

d_c = [1,1,-1,-1,2,-2,2,-2]
d_r = [2,-2,2,-2,1,1,-1,-1]
#행,열
col, row = int(data[1]), int(ord(data[0]))-int(ord('a'))+1

count = 0

for search in range(8):
    n_c = col + d_c[search]
    n_r = row + d_r[search]
    if n_c >= 1 and n_c <= 8 and n_r >=1  and n_r <= 8:
        count += 1

print(count)


#문제 해설:
#d_c와 d_r이 tuple로 묶고 그 index를 for문에서 찾아준 후 그 위치를 다시 step[0] 과 step[1]로 접근 하였다.