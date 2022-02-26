def factorial(num): 
    if num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

num = int (input("Digite um número natural: ")); 

print(factorial(num)) 