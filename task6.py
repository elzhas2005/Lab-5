import re 
x = str(input())
y = re.sub("[ ,.]", ":", x )
print(y)