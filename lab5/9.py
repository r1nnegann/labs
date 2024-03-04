import re

string = re.sub(r'[A-ZА-Я][^ A-ZА-Я]+', lambda x: f'{x.group()} ', input())
print(string)