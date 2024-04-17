with open(texto) as fh:
    count = 0
text = fh.read()
for character in text:
    if character.isupper():
        count +=1

