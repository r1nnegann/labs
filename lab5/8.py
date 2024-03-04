import re

string = re.split(r'[A-ZА-Я]', input())
print([i for i in string if i])