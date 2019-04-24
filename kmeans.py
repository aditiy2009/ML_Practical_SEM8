import math
import matplotlib.pyplot as plt

input_points=[[0.1, 0.6, 0], [0.15, 0.71, 0], [0.08, 0.9, 0], [0.16, 0.85, 0], [0.2, 0.3, 0], [0.25, 0.5, 0],
                [0.24, 0.1, 0], [0.3, 0.2, 0]]

cnt_ans1,cnt_ans2=-1,-1
centroid1=input_points[0]
centroid2=input_points[7]

def cluster_decision(x2,y2):
    d1=math.sqrt((x2-centroid1[0])**2+(y2-centroid1[1])**2)
    d2=math.sqrt((x2-centroid2[0])**2+(y2-centroid2[1])**2)

    if d1<d2:
        return 1
    else:
        return 2

def calc_mean():
    mean1=[0.0,0.0]
    mean2=[0.0,0.0]
    sum1=[0.0,0.0]
    sum2=[0.0,0.0]
    count1=0
    count2=0

    for point in input_points:
        if(point[2]==1):
            sum1[0]+=point[0]
            sum1[1]+=point[1]
            count1+=1
        elif(point[2]==2):
            sum2[0]+=point[0]
            sum2[1]+=point[1]
            count2+=1
        else:
            assert False
    mean1[0]=sum1[0]/count1
    mean1[1]=sum1[1]/count1
    mean2[0]=sum2[0]/count2
    mean2[1]=sum2[1]/count2

    global cnt_ans1,cnt_ans2
    cnt_ans1=count1
    cnt_ans2=count2

    return mean1,mean2

while True:
    for point in input_points:
        point[2]=cluster_decision(point[0],point[1])

    previous_c1=centroid1
    previous_c2=centroid2

    centroid1,centroid2=calc_mean()

    if previous_c1==centroid1 or previous_c2==centroid2:
        break

for point in input_points:
    print(point)

print("c1 cluster population : ",cnt_ans1)
print("c2 cluster population : ",cnt_ans2)
print("c1 point : ",centroid1)
print("c2 point : ",centroid2)

for point in input_points:
    plt.scatter(point[0],point[1],color="g")
plt.show()

plt.scatter(centroid1[0],centroid1[1],color="r")
plt.scatter(centroid2[0],centroid1[1],color="b")
plt.show()

for point in input_points:
    plt.scatter(point[0],point[1],color="g")


plt.scatter(centroid1[0],centroid1[1],color="r",marker="*")
plt.scatter(centroid2[0],centroid1[1],color="b",marker="*")
plt.ylabel('y')
plt.xlabel('x')
plt.title("kmeans")
plt.show()
