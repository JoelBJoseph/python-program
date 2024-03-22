import math

radius = int(input('Enter the radius of the circle: '))

circumference = 2*radius*math.pi
area = math.pi*(radius**2)

print('Circumference :', circumference,"m")
print('Area :', area, "sq m")

# OUTPUT:
#     Enter the radius of the circle: 2
#     Circumference : 12.566370614359172 m
#     Area : 12.566370614359172 sq m