
Untitled2.ipynb_
 
import numpy as np
import matplotlib.pyplot as plt 
​
​
​
def estimation(x,y):
  a=sum(x)  #sum of array x
  b=sum(y)  #sum of array y
​
  lin=sum(numpy.array(x)**2)  #sum of squares of array elements
​
  mul=sum(i*j for i,j in zip(x,y))  #zip: (10,95) (9,80) multiply x[i] y[i]
​
  m=(b*lin - a*mul)/((8*lin) - (a**2))  #formula for slope in linear regression
  c=(8*mul - a*b)/((8*lin) - (a**2))  #formula for constant
  return(m,c)
​
​
​
def plot_graph(x,y,b):
   plt.scatter(x, y, color = "m", marker = "o", s = 30)
   y_pred = b[1]*x + b[0]
  
   plt.plot(x, y_pred, color = "g") 
​
   plt.xlabel('x') 
   plt.ylabel('y') 
 
   plt.show()   
​
def main():
  x=np.array([10,9,2,15,10,16,11,16])
  y=np.array([95,80,10,50,45,98,38,93])
  
  b= estimation(x,y)
  print("Estimated coefficients:\nb_0 = {}  \nb_1 = {}".format(b[0], b[1])) 
  plot_graph(x,y,b)
  
main()
