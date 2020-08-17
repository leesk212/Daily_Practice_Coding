Y,M,D = map(int,input().split("."))

if Y < 1000:
    if Y < 100:
        if Y < 10:
            year = "000"+str(Y)
        else:
            year = "00"+str(Y)
    else:
        year = "0"+str(Y)
else:
    year = str(Y)

if M < 10:
    month = "0"+str(M)
else:
    month = str(M)
if D < 10:
    day = "0"+str(D)
else:
    day = str(D)
    
print(year+"."+month+"."+day)
