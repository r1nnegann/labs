a = input()
lower_letters = 0
for i in a:
    if i!=i.upper():
        lower_letters += 1
upper_letters = len(a)-lower_letters
print("upper -", upper_letters)
print("lower -", lower_letters)