import math

x1,y1=map(float,input().split())

x2,y2=map(float,input().split())



xf = (x2-x1)**2
yf= (y2-y1)**2
d = math.sqrt(xf+yf)
print("{:.4f}".format(d))
