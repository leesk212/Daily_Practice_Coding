def f(x):
    return {'A':'best!!!','B':'good!!','C':'run!','D':'slowly~'}.get(x,'what?')
data = input()
print(f(data))

