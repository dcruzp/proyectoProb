import numpy as np 
import math
import random as rdm

def funcionInversa (y , l , a):
    return (math.log (1-y) / -l)**(1/a)

def SimulaciondelafuncionInversa (l , a ):
    Y = rdm.random()
    return funcionInversa(Y,l,a)