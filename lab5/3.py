import re

string = re.findall(r'[a-zа-я]+_[a-zа-я]+', input())
print(*string)