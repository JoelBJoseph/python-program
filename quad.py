import cmath

print("---  ax^2 + bx + c  ---")
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

#   calculating the discriminant
d = b**2 - 4*a*c

solution1 = (-b + cmath.sqrt(d))/(2*a) 
solution2 = (-b - cmath.sqrt(d))/(2*a)

if solution1 == solution2:
    print("The solution is", solution1)
else:
    print("The solutions are", solution1,"and",solution2)
    
    
# OUTPUT:
#     Enter a : 1
#     Enter b : 2
#     Enter c : 1
#     The solution is (-1+0j)