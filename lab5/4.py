import re

string = re.findall(r'[A-ZА-Я][а-яa-z]+', input())
print(*string)