import re

string = re.findall(r'ab{2,3}', input())
print(*string)
