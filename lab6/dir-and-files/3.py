import os

adress = input('path: ')
splt = adress.split('\\')[1:] # надеюсь не ошибка
adress2 = 'C:\\'
if os.path.exists(adress):
    for i in splt:
        adress2 = os.path.join(adress2, i)
        print(f'{i} - directory, files - {os.listdir(adress2)}')
