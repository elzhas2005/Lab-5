import re
x = str(input())
y = '^[a-z]+(_[a-z]+)*'
z = re.search(y, x)
print(z)