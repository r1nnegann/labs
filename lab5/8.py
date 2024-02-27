import re

string = re.sub(r'([A-ZА-Я])([A-ZА-Я])', lambda x: f'{x.group(1)} {x.group(2)}', input())
print(string)