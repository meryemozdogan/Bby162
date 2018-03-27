kadinismi = input("Bir kadın adı giriniz...:")
erkekismi = input("Bir erkek adı giriniz...:")
mısra    = int(input("Mısra sayısı giriniz...Maksimum 9 mısra yazdırılabilir.."))


import random

sarki = [erkekismi + " bugün bende bir hal var " , kadinismi + " ürkek ürkek bakar"  , "Yağmur iri iri düşer toprağa " , erkekismi + " seni görmemeli" , " Açma pencereni perdeleri çek ", " anla " + erkekismi + " ben bir deliyim " , " bir mumun ardında bekleyen " + kadinismi ,  " Zambaklar en ıssız yerlerde açar " , erkekismi + " Denizin dibinde geziyor gibi "," Ellerin, ellerin ve parmakların ", " Zaman ne de çabuk geçiyor " , kadinismi + " Akşamları gelir ", erkekismi + " Saat onikidir söndü lambalar " , kadinismi  + " Siyah güller, ak güller... "]

for olusturulacak_sarki in sarki[:mısra]:
    print(random.choice(sarki))


if mısra > 9:
    print("Geçerli bir mısra sayısı girmediniz..")
    print("Yazdırılan mısra sayısı: 10")

else:
    print("Yazdırılan mısra sayısı:", mısra)
