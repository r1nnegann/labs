import os

adress = input("path: ")
os.chdir(adress)
only_dir, only_files = [], []
all_files = os.listdir(adress)
for i in all_files:
    if os.path.isdir(i):
        only_dir.append(i)
    else:
        only_files.append(i)
print(only_files, "- files")
print(only_dir, "- directories")
print(all_files, "- all files")