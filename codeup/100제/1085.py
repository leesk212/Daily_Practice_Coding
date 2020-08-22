f,s,t,forth = map(int,input().split())

print ("%.1f MB" % (float(f*s*t*forth) / (8.0* 1024.0 * 1024.0)))