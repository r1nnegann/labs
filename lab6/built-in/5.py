from random import randint
stavka = int(input('ваша ставка: '))
koef = int(input("коэффициент ставки: "))
kortezh = tuple((randint(0,1) for _ in range(koef)))
print(f"в этот раз выиграл {stavka * koef}" if all(kortezh) else "проиграл лудоман")
