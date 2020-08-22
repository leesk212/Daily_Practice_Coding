a = str(input())
return_data = str()

for s in range(ord('a'),ord(a)+1):
    return_data = return_data + chr(s) + " "

print(return_data)