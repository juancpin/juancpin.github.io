#!/usr/bin/env python3
import math
#import numpy


#preguntar por qué math.log no acepta tuplas
def f1(x):
    loga = math.log10(x)
    print ('LOG de', x ,'es', loga, sep=' ')
    return x
    #x = list(zip(*x))
    #x = zip(*x)
    
#f1(1)

x = (1000)
print(type(x))
f1(x)
