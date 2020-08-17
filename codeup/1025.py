data = list(map(str, input()))

for index in range(len(data)-1):
    print_zero = "0"
    for zero_plus in range(3-index):
        print_zero = print_zero + "0"
    print("["+data[index]+print_zero+"]")
print("["+data[len(data)-1]+"]")

