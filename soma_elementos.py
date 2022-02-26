def soma_elementos(list):
    soma = 0
    for i in list:
        soma = soma + i
    return soma
array = [5,6,7,11]
print(soma_elementos(array))