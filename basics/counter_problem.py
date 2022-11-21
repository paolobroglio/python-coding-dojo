from collections import Counter

shoes_number = int(input())
shoes_sizes = Counter(list(map(int,input().split()))) 
customers_number = int(input())
revenue = 0
for i in range(0, customers_number):
    inputs = list(map(int,input().split()))
    size = inputs[0]
    value = inputs[1]
    if shoes_sizes.get(size, 0) > 0:
        shoes_sizes[size] -= 1
        revenue += value
print(revenue)
