def raizes(a, b, c):
    delta = (b*b - 4*a*c)
    print('o delta é:', delta)
    x1 = (-b + delta**(1/2)) / (2*a)
    x2 = (-b - delta**(1/2)) / (2*a)
    print('-'*30)
    
    if delta<0:
        print('Esta equação não possui raízes reais.')
    elif delta==0:
        print('Esta equação possui apenas uma raíz:')
        print(x1)
    else:
        print('As raízes da equação são:'.format(x1, x2))


#Main

a = int(input('digite o A:'))
b = int(input('digite o B:'))
c = int(input('digite o C:'))

print(f'{a}x{b}x{c}')
print('-'*30)


raizes(a,b,c)


#codigo sem def
'''
a = int(input('digite o A:'))
b = int(input('digite o B:'))
c = int(input('digite o C:'))
print(f'{a}x{b}x{c}')
print('-'*30)

delta = (b*b - 4*a*c)
print('o delta é:', delta)
x1 = (-b + delta**(1/2)) / (2*a)
x2 = (-b - delta**(1/2)) / (2*a)
print('-'*30)
    
if delta<0:
    print('Esta equação não possui raízes reais.')
elif delta==0:
    print('Esta equação possui apenas uma raíz:')
    print(x1)
else:
    print('As raízes da equação são:'.format(x1, x2))

'''


