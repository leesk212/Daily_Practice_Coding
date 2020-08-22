data = list( map(int, input().split()) )
data = sorted(data)
end = data[2]


while True:
    if end % data[0] == 0 and end % data[1] == 0 and end % data[2] == 0:
        print(end)
        break
    end = end + 1


