import re 
x = str(input())
y = '^[A-Z][a-z]+$'
z = re.search(y, x)
print(z)