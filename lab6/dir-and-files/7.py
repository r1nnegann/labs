with open('f1') as f1, open('f2', 'w') as f2:
    f2.writelines(f1.readlines())