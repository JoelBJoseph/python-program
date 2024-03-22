# distance b/w two points (x1, y1) and (x2, y2)
# d^2 = (x2- x1)^2 + (y2-y1)^2
import math

x1 = int(input("Enter x1 : "))
y1 = int(input("Enter y1 : "))

x2 = int(input("Enter x2 : "))
y2 = int(input("Enter y2 : "))

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("\nThe distance is ", distance,"m")

# OUTPUT:
#     Enter x1 : 2
#     Enter y1 : 3
#     Enter x2 : 1
#     Enter y2 : 5

#     The distance is  2.23606797749979 m