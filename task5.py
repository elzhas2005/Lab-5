import re
x = str(input())
y = '^a(.*)b$'
z = re.search(y, x)
print(z.string)