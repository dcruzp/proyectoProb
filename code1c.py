import random as rdm
import numpy as np  
import math


def exponencial (l):
    U = rdm.random()   
    return -1 / l * np.log(U) 

def simulacionNormal (miu , sigma ):
    U = rdm.random()
    Y = exponencial(1) 

   
    while U > math.pow(math.e , (-1)*(math.pow(Y-1,2)/2)):
        U = rdm.random() 
        Y = exponencial(1) 

    U2 = rdm.random(); 

    if U2 > 0.5:
        Y = -Y

    return (Y * sigma) + miu      


s = 1000 

def promedio (miu , sigma , s):
    promedio = 0 
    for i in range (s):
        promedio += simulacionNormal(miu,sigma)
    return promedio / s      

print (promedio (1,3 , s))