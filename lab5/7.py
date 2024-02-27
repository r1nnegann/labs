import re

string = re.sub(r'_.', lambda x: x.group()[1].upper(), input())
print(string)