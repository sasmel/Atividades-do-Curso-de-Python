def remove_repetidos(array):
    l = []
    for i in array:
        if i not in l:
            l.append(i)
    l.sort()
    return l

array = [2,2,4,5,7,7,7,8,5,10,11,11]

array = remove_repetidos(array)
print (array)