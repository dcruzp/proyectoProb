import numpy as np 
import random as rdm 

def Bernoulli (p):
    U = rdm.random() 
    if U <= p :
        return 1 
    else:
        return 0

def GeometricSimulation (p):
    count = 1
    while Bernoulli(p) != 1 :
        count = count +1 
    return count 

def promedio (p , n ):
    promedio = 0 
    for i in range(n):
        promedio += GeometricSimulation(p) 
    return promedio /n          

n = 1000   #numero de simulaciones 
table = [1/2,1/3,1/4,1/5] 

for x in table: 
    print ('landa ' + str (x) + 'promedio ' + str(promedio(x , n)))