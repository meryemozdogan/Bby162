print("Adam Asmaca Oyununa Hoşgeldin!\nToplam 5 hakkın var, bol şans.\n ")
import random

kalanHak = 5
i = 0

kelime = random.choice(['zeus','afrodit','athena','poseidon','hades'])
harfHavuzu = []
for islem in kelime:
    harfHavuzu.append("_")
print(harfHavuzu)
while kalanHak > 0:
    yazılanHarf = input("Bir harf giriniz:").lower()
    if yazılanHarf in kelime:
        for kontrol in kelime:
            if kelime[i] == yazılanHarf:
                harfHavuzu[i] = yazılanHarf
            i+=1
        print(harfHavuzu)
        i=0
    else:
        i=0
        kalanHak -= 1
        print("Kalan can " + str(kalanHak) )

    if kalanHak == 0:
        print('Öldün çık. Doğru kelime "{}" idi.\n'.format(kelime))
        break
