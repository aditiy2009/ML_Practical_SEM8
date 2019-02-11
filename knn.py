import pandas as pd
data=pd.read_csv("knn.csv")
import math
class dis:
    dist=0
    x=0
    y=0
    p=0
k=int(input("Enter k:"))
x=int(input("Enter x:"))
y=int(input("Enter y:"))

i=0
distance=[]
for i in range(len(data)):
    d=dis()
    d.dist=math.sqrt(math.pow((x-data.iloc[i,0]),2) + math.pow((y-data.iloc[i,1]),2) )
    d.x=data.iloc[i,0]
    d.y=data.iloc[i,1]
    d.p=data.iloc[i,2]
    distance.append(d)

distance = sorted(distance, key=lambda dis: dis.dist)
n=0
y=0
for i in range(k):
    if distance[i].p==0:
        n=n+1
    else:
        y=y+1

if y>n:
    print("predicted Class:","yes")
else:
    print("predicted Class:","no")

