import math
import random

rands = random.randint(1,10)
i=0
print(rands)
list1 = list()
while i < rands:
    rand2=random.randint(1,1000)
    list1.append(rand2)
    i += 1

print(list1)
