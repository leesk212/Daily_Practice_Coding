w,h,b = map(int,input().split())

print("%.2f MB" %(float(w*h*b) / (8.0*1024.0*1024.0)) )
