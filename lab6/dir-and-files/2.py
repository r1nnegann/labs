import os

adress = input("path: ")
if os.access(adress, os.F_OK):
    print("file exists")
    print('readable' if os.access(adress, os.R_OK) else 'not readable')
    print('writable' if os.access(adress, os.W_OK) else 'not writable')
    print('executable' if os.access(adress, os.X_OK) else 'not executable')
else:
    print("file doesnt exist")