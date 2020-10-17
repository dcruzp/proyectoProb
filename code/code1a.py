import numpy as np 
import random as rdm

def exponencial (l):
    U = rdm.random()   
    return -1 / l * np.log(U) 

def gammasimulation (l , n ): # lambda , numero de llamadas
    total = 0 
    for i in range (n):
        total += exponencial(l)
    return total     


def media (l,n,s): #lambda , numero de llamadas , cant de simulaciones
    promedio = 0 ;
    for i in range (s):
        promedio += gammasimulation(l,n)
    return promedio / s     

s = 1000 # numero de simulaciones 

table = [[1/2 , 30 , s ],
         [1/4 , 20 , s ],
         [1/6 , 10 , s ],
         [1/8 , 36 , s ],]

for x in table :
    print ( '(landa= ' + str(x[0])  + ' , numero de llamadas ' + str(x[1]) + ' media -> ' + str(media(x[0],x[1],x[2])) )
