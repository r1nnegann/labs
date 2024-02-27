import re

string = re.findall(r'ab+', input())
print(*string)