import math
import random as rdm


def funcionInversa (y):
    if y < 1/2:
        return 1/2 * math.log(2*y)
    else :
        return -0.5 * math.log(-2*y+2) 


def SimulaciondelafuncionInversa ():
    return funcionInversa(rdm.random())