def rev_frase(frase):
    palabras = frase.split(' ')
    reves_frase = ' '.join(reversed(palabras))
    return reves_frase

if __name__ == "__main__":
    input = 'No te lo crees ni tú'
    print (rev_frase(input))