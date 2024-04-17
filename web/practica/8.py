n=int(input('Introduzca cuántos items de la serie FIbonnaci quieres ver: '))
first = 0
second = 1
sum = 0
count = 1
print ('Fibonacceando:')
while (count<=n):
    print(sum)
    count += 1
    first = second
    second = sum
    sum = first + second
    