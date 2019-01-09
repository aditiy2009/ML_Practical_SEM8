import numpy

x=[10,9,2,15,10,16,11,16]
y=[95,80,10,50,45,98,38,93]

a=sum(x)	#sum of array x
b=sum(y)	#sum of array y

lin=sum(numpy.array(x)**2) 	#sum of squares of array elements

mul=sum(i*j for i,j in zip(x,y))	#zip: (10,95) (9,80) multiply x[i] y[i]

m=float((b*lin - a*mul))/float(((8*lin) - (a**2)))	#formula for slope in linear regression
c=float((8*mul - a*b))/float(((8*lin) - (a**2)))	#formula for constant

print ("value of slope:",m)
print ("value of constant:",c)


