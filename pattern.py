n = int(input("Enter the range"))

for i in range(n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()  


# OUTPUT:
#     Enter the range: 4

#         1
#         1 2
#         1 2 3
#         1 2 3 4