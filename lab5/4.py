import re

string = re.findall(r'[A-Z][a-z]+', input())
print(*string)