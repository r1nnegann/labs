import re

string = re.findall(r'[a-zA-Zа-яА-Я]+_[a-zA-Zа-яА-Я]+', input())
print(*string)