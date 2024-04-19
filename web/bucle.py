import math
import random

a = random.randint(1,1000000000)
print ('Empezamos por', a)
while a > 3:
    a /=2
    #dejamos 2 decimales
    print (round (a, 2))
