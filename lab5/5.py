import re

string = re.findall(r'a.+b', input())
print(*string)