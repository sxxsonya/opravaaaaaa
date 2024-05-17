import random

pocet_zivotu = 2

opakovani = 1

body = 0

pocet_kol_print = 0

pocet_kol = random.randint(1,15)

min_otazek = pocet_kol/2

for y in range(pocet_kol):
    pole_random = []

    lenght = random.randint(1,10)

    for x in range(lenght):
        pole_random.append(random.randint(1,10))

    print (pole_random)

    pocet_kol_print = pocet_kol_print + 1

    print ("Kolo", pocet_kol_print, "z", pocet_kol)

    delka = int(input("zadej delku pole: "))

    if delka == lenght:
        body = body + 1
        print ("spravne, mas", body, "bodu")
    else:
        body = body
        print ("Chyba, mas", body, "bodu")

if min_otazek > body:
    pocet_zivotu = pocet_zivotu - 1
    print ("ztratil jsi 1 zivot")
else:
    pocet_zivotu = pocet_zivotu

print("Mate", pocet_zivotu, "zivotu")

print("Mate", body, "bodu")

if pocet_zivotu == 2:
    print ("budes chcit opakovat kolo??")

if pocet_zivotu == 0:
    print ("GAME OVER ty dylino")