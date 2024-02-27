import re

string = re.sub(r'[ ,.]', ':', input())
print(string)