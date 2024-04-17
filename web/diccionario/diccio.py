#!/usr/bin/env python3
import pickle
from pathlib import Path

d = dict()

file_name = input('Nombre de archivo: ')

path = Path(file_name)
if path.is_file():
    input_file = open(file_name, "rb")
    d = pickle.load(input_file)
    input_file.close()
else:
    print('No existe el archivo, se creará a continuación')
    
document_number = input('Introduce DNI: ')

if document_number in d:
    print('La edad de' + document_number + 'es' + str(d[document_number]))
else:
    age = ('No existe, se añade. Introduce edad tb: ')
    if age.isnumeric():
        num = int(age)
        d[document_number] = num
        print('Añadido al diccionario')
        
    
output_file = open(file_name, "wb")
pickle.dump(d, output_file)
output_file.close()    