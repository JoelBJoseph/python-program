def count(array):
    odd_count = 0
    for element in array:
        if(element % 2 != 0):
            odd_count += 1
            
    return odd_count 

n = int(input('Enter the limit: '))
a = []
print("Enter the number: ")
for i in range(0,n):
    add = int(input())
    a.append(add)
odd = count(a)

even_count = n - odd

print("Even count: ",even_count)
print("Odd-count: ",odd)

# OUTPUT:
#     Enter the limit: 3
#     Enter the number:
#     12
#     5
#     3
#     Even count:  1
#     Odd-count:  2