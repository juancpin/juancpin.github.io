import math
x=233
def desc(x):
    #print('n', x)
    while x > 3: 
        if x % 2 == 0:
           print(x)
        else:
            x -= 1 
        x /= 2   
        

desc(x)

