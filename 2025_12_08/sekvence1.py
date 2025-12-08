brojevi = range(1,5) # 1, 2, 3, 4
for broj in brojevi:
    print(broj)
    #     01234
poruka = "Hello"
    #          0, 5           -> 0, 1, 2, 3, 4
for x in range(0, len(poruka)): 
    # prolazak kroz opseg, brojeve koristimo za pozicije
    print(poruka[x])

for slovo in poruka: # prolazak kroz clanove kolekcije
    print(slovo)

#poruka[0] = "P" - string je nemutabilan

poruka = "Zdravo kako ste"
print(len(poruka))

# print(poruka[0])
# print(poruka[1])
# print(poruka[2])
# print(poruka[3])
# print(poruka[4])

poruka = "Hello World"
print(poruka.upper())
print(poruka.lower())
print(poruka.capitalize())

brojevi = [3, 10, 12, 2, 7]
for broj in brojevi:
    print(broj)

for x in range(0, len(brojevi)):
    print(brojevi[x])
                    # 0         1            2
korisnicka_imena = ["gost54", "petar123", "jovana555"]
for x in range(len(korisnicka_imena)):
    print(korisnicka_imena[x])

#korisnicka_imena[3] = "marko" ne moze
korisnicka_imena.append("marko")
print(korisnicka_imena)
korisnicka_imena[1] = "marija"
print(korisnicka_imena)

korisnicka_imena.remove("marija")
print(korisnicka_imena)
korisnicka_imena.pop(0)
print(korisnicka_imena)
del korisnicka_imena[0]
print(korisnicka_imena)

# 0 petar, 1 ana, 2 jovana
korisnici = ["petar", "ana", "jovana", "marko", "jovan", "milica"]
for i in range(len(korisnici)):
    print(f"Indeks: {i}, Vrednost: {korisnici[i]}")

for indeks, vrednost in enumerate(korisnici):
    print(f"Indeks: {indeks}, Vrednost: {vrednost}")

izdvojeni_korisnici = korisnici[1:5]
print(izdvojeni_korisnici)
