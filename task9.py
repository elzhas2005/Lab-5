import re
x = str(input())
y = re.sub(r"(\w)([A-Z])", r"\1 \2", x)
print(y)