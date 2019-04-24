import pandas as pd
import math
import matplotlib.pyplot as plt

def mean_calc(X,Y):

    xmean=sum(X)/len(X)
    ymean=sum(Y)/len(Y)

    print("Mean at x : ",xmean)
    print("Mean at y : ",ymean)

    return xmean,ymean

def correlation(X,Y):

    xy=[(x*y) for (x,y) in zip(X,Y)]
    x_sq=[(x**2) for x in X]
    y_sq=[(y**2) for y in Y]

    xsum,ysum,x_sq_sum,y_sq_sum,xy_sum=sum(X),sum(Y),sum(x_sq),sum(y_sq),sum(xy)

    r=(len(X)*xy_sum - xsum*ysum)/(math.sqrt((len(X)*x_sq_sum-xsum**2)*(len(X)*y_sq_sum-ysum**2)))

    print("Value of correlation between x and y is : ",r)

    return r

def find_coefficients(X,Y,xmean,ymean):
    cov=0
    var=0

    for i in range(len(X)):
        cov+=(X[i]-xmean)*(Y[i]-ymean)
        var+=(X[i]-xmean)**2

    m=cov/var

    c=ymean - m*xmean

    print("Equation of line is : y=",m,"x+",c)
    return m,c

def residual_error(X,Y,ymean,m,c):
    sst=0
    sse=0

    for i in range(len(X)):
        yp=X[i]*m + c

        sst+=(Y[i]-ymean)**2
        sse+=(Y[i]-yp)**2

    r2=1-(sse/sst)

    print("accuracy of model is : ",r2*100)
    return r2

def for_any_x(X,Y,m,c):
    x=float(input("Enter value of x :"))
    y=0

    for i in range(len(X)):
        if x==X[i]:
            y=Y[i]

            print("Actual value of x and y are : ",x," ",y)

    yp=m*x+c
    print("for x = ",x," value of y is : ",yp)
    print("difference between actual value and predicted value is : ",abs(yp-y))

def main():

    data=pd.read_csv('salary.csv')
    X=data['YearsExperience'].values
    Y=data['Salary'].values

    print("=======================================================================================")
    print("using 75% data")
    data1=data.sample(frac=0.75)
    X1=data1['YearsExperience'].values
    Y1=data1['Salary'].values
    mx1,my1=mean_calc(X1,Y1)
    correlation(X1,Y1)
    m1,c1=find_coefficients(X1,Y1,mx1,my1)
    r21=residual_error(X1,Y1,my1,m1,c1)
    yp1=m1*X1+c1
    print("========================================================================================")

    print("=======================================================================================")
    print("using 80% data")
    data1=data.sample(frac=0.80)
    X2=data1['YearsExperience'].values
    Y2=data1['Salary'].values
    mx2,my2=mean_calc(X2,Y2)
    correlation(X2,Y2)
    m2,c2=find_coefficients(X2,Y2,mx2,my2)
    r22=residual_error(X2,Y2,my2,m2,c2)
    yp2=m2*X2+c2
    print("========================================================================================")


    print("=======================================================================================")
    print("using full data")
    mx,my=mean_calc(X,Y)
    correlation(X,Y)
    m,c=find_coefficients(X,Y,mx,my)
    r23=residual_error(X,Y,my,m,c)
    yp=m*X+c
    print("========================================================================================")

    if r21>r22:
        if r21>r23:
            print("First line with data 75% is best fit")
        else:
            print("Line with full data is best fit")
    else:
        if r22>r23:
            print("Second line with 80% is best fit")
        else:
            print("Line with full data is best fit")

    plt.scatter(X,Y,color="orange",marker="*",label="points of dataset")
    plt.plot(X1,yp1,color="b",label="75% data line")
    plt.plot(X2,yp2,color="r",label="80% data line")
    plt.plot(X,yp,color="g",label="full data")
    plt.xlabel('salary')
    plt.ylabel('Years of Experience')
    plt.legend()
    plt.show()
    for_any_x(X,Y,m,c)
main()
