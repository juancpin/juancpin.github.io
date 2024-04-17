def sumalista(num_Lista):
    if len(num_Lista) == 1:
        return num_Lista[0]
    else:
        return num_Lista[0] + sumalista(num_Lista[1:])
    
print(sumalista([3, 5, 8, 9, 9]))