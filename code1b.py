import matplotlib.pyplot as plt 
import numpy as np 
from scipy import stats 
#import seaborn as sns 

#Graficando geometrica 
p = 0.3 # paramtro de forma 

geometrica  = stats.geom(p); 

x = np.arange(geometrica.ppf(0.01) , geometrica.ppf(0.99))
print(x) 
fmp = geometrica.pmf(x); #Funcion de masa de probabilidad 

plt.plot(x , fmp , '--'); 
plt.vlines(x,0,fmp , colors ='b' , lw = 5 , alpha = 0.3) 

plt.title ( 'Distribucion Geometrica con parametro  p = 0.5 '  )
plt.ylabel ('P (X = x)') 
plt.xlabel ('(X = x)')
plt.savefig('gafica1b.png')
plt.show() 