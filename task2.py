import re
x = str(input())
y = '.*a(b{2,3})'
z = re.search(y, x)
print(z.string)