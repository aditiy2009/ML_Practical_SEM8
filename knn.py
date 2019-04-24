import math
import matplotlib.pyplot as plt
import pandas as pd

def create_dataset():
    d={'x':[158,158,158,160,160,163,163,160,163,165,165,165,168,168,168,170,170,170],'y':[58,59,63,59,60,60,61,64,64,61,62,65,62,63,66,63,64,68],'class':["M","M","M","M","M","M","M","L","L","L","L","L","L","L","L","L","L","L"]}
    df=pd.DataFrame(data=d,columns=['x','y','class'])

    hm_x=[]#height with medium class
    wm_y=[]#weight with medium class
    hl_x=[]#height with large class
    wl_y=[]#weight with large class

    for index,row in df.iterrows():
        if row['class']=="M": #check if class is M or not
            hm_x.append(row['x'])
            wm_y.append(row['y'])
        else:
            hl_x.append(row['x'])
            wl_y.append(row['y'])

    return df,hm_x,hl_x,wm_y,wl_y

def find_class(df,x,y,k):
    dic={}

    for index,row in df.iterrows():
        dist=math.sqrt((row['x']-x)**2+(row['y']-y)**2)#calculating distance
        dic[index]=dist #storing data

    sorted_dist=sorted(dic.items(),key=lambda kv:kv[1])#sorting data

    list_k=[] #data collected as per value of k
    for i in range(k):
        list_k.append(sorted_dist[i][0])

    labels=[]#giving back class name to collected data

    for index,row in df.iterrows():
        if index in list_k:
            labels.append(row['class'])

    medium=0#count of medium size
    large=0#count of large size

    for v in labels:
        if v=="M":
            medium+=1
        else:
            large+=1

    if (medium>large):
        print("predicted class is medium")
    elif( large>medium):
        print("preddicted class is large")
    else:
        print("You can choose any of M and L both will fit")

def main():
    k=int(input("enter value of k : "))
    x=int(input("enter your height in cms : "))
    y=int(input("enter weight in kgs : "))
    df,hm_x,hl_x,wm_y,wl_y=create_dataset()
    find_class(df,x,y,k)

    plt.scatter(hm_x,wm_y,color="b",label="medium class data")
    plt.scatter(hl_x,wl_y,color="g",label="large class data")
    plt.scatter(x,y,color="orange",marker="*",label="predicted data point")
    plt.legend()
    plt.xlabel('height in cms')
    plt.ylabel('weight in kgs')
    plt.xlim(150,190)
    plt.ylim(50,80)
    plt.show()
main()
