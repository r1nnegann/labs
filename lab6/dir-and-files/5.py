li = [str(i) for i in range(10)]
with open('text.txt', 'w') as file:
    file.writelines(li)