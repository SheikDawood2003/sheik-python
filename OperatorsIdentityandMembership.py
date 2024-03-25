#Identity operator

x1 = ['apple','banana']
y1 = ['apple','banana']
z1 = x1

print(x1 is y1)
print(x1 is not y1)
print(y1 is not x1)
print(x1 is z1)

#Membership operator
x2 = 'Cherry'

print('C' in x2)
print('Z' not in x2)