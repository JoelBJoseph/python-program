def fact(n):
    factorial = 1
    if n == 1 or n == 0:
        factorial *= 1
    else:
        factorial *= n * fact(n-1)
    
    return factorial


n = int(input('Enter the  limit: '))
x = int(input('Enter the value of x: '))
sign = -1
cos = 1

for i in range (n):
    cos += ((-1) ** i) * (x ** (2 * i)) / fact(2 * i)
    sign = - sign
    
print(cos)

# OUTPUT:
#     Enter the  limit: 4
#     Enter the value of x: 45
#     -11363158.9375