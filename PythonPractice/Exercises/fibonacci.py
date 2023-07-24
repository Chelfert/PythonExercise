#ask user how many fibonacci numbers to generate
#1,1,2,3,5,8,13


def fib(n):
    
    a = 0
    b = 1
    
    if n == 1:
        print(a)
        
    else:
    
        print (a)
        print(b)
    
        for i in range(2,n):
        
            c = a+b
            a = b
            b = c
            print(c)

user_input = int(input("How many fibonacci numbers would you like to generate?: "))
fib(user_input)