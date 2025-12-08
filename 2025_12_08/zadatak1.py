#    0  1  2
a = [1, 2, 3]
b = [4, 5, 6]

zbir = []

#print(a + b) nadovezuje liste
for i in range(len(a)):
    zbir.append(a[i] + b[i]) # dodaje clan u listu zbir

print(zbir)
zbir.clear() # uklanja sve clanove liste
print(zbir)

# korisnicko ime mora imati 5 ili vise karaktera (i ne sme da ima razmake)
registrovani_korisnici = ["jovana", "a n a", "x", "marijana123"]
ispravna_imena = []

for korisnik in registrovani_korisnici:
    formatirano_ime = korisnik.replace(" ", "") #.strip() sa kraja i pocetka uklanja " "
    if len(formatirano_ime) >= 5:
        ispravna_imena.append(formatirano_ime)
    else:
        print(f"Neispravno: {korisnik}")

print(ispravna_imena)
ispravna_imena.sort()
print(ispravna_imena)

# [5, 1, 2, 7, 4]
# [ 1, 2, 4, 5, 7] 
# ime korisnika              poeni
# korisnik,          test 1 , test 2, test 3
# ana                85         90     60
# jovana             75        60     90
korisnik1 = ["ana", 85, 90, 60, 55]  # korisnik1[0]
korisnik2 = ["jovana", 75, 60, 90]   # korisnik2[0]
#                   0                       1
# polaznici = [["ana", 85, 90, 60, 55], ["jovana", 75, 60, 90]]
polaznici = [korisnik1, korisnik2]
# ana = polaznici[0]
# jovana = polaznici[1]

for polaznik in polaznici:
    # print(polaznik)
    for informacija in polaznik:
        print(informacija)
    print("##############")

# print(ana[2])
# print(jovana[1])
# # prikazi 85
# print(polaznici[0][1])
# # prikazi 75
# print(polaznici[1][1])

korpa = [
    ["patike adidas", 15000, 1], 
    ["patike nike", 13000, 2]
    ]

print(f"Ukupno proizvoda u korpi: {len(korpa)}")
# Ispisi detalje clanova korpe
for proizvod in korpa:
    for informacija in proizvod:
        print(informacija)
    print("***************")