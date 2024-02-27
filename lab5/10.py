import re

string = re.sub(r'[A-ZА-Я]', lambda x: f'_{x.group()}', input())
print(string)