def isPrimo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True

def app():
    num = int(input('Introduczca un nº: '))
    result = isPrimo(num)

    if result is True:
        print('Es un nº Primo')
    else:
        print('No es un nº Primo')

if __name__ == '__main__':
    app()