n = int(input('Enter the length of the sequence: '))

next_number_int = 0

x1 = 1

x2 = 2

x3 = 3

print(x1)

print(x2)

print(x3)

for i in range(4,n+1):
    next_number_int = x1+x2+x3
    x1=x2
    x2=x3
    x3=next_number_int
    print(next_number_int)