age = 10
# prikazi igru ako ima vise od 13 godina
print(age > 13) # True / False
if age > 13: 
    print("Prikazi sadrzaj")
    print("Pokrenuta je igra")

print("Prva sledeca linija")

email_baza = "korisnik@gmail.com"
sifra_baza = "123"

uneti_email = "korisnik@gmail.com"
uneta_sifra = "123"

# Ispisi uspesno logovanje ako su ispravni i email i sifra
if email_baza == uneti_email and sifra_baza == uneta_sifra:
    print("Uspesno logovanje!!!")

brzina_vozila = 80
ogranicenje = 50
urucena_kazna = True

if brzina_vozila > 50:
    if urucena_kazna == True:
       print("Dodajte kaznene poene") 
    
    print("Posaljite kaznu")


# prikazati uspesno ili neuspesno u zavisnosti od ispravnih podataka
if uneti_email == email_baza and uneta_sifra == sifra_baza:
    print("Uspesno logovanje")
else:
    print("Neispravni podaci")

print("Izvrsava se u svakom slucaju")


novac_na_racunu = 1200
cena_proizvooda = 500

# Uspesna / Neuspesna kupovina 
if novac_na_racunu >= cena_proizvooda:
    print("Uspesna kupovina!!!")
    novac_na_racunu -= cena_proizvooda
    print(f"Novo stanje na racunu: {novac_na_racunu}")
else:
    print("Nemate dovoljno novca na racunu.")


# Kanban
# Prikazujemo razlicitu boju taskova i raspored u zavisnosti od dana u nedelji
dan_u_nedelji = "ponedeljak"

if dan_u_nedelji == "ponedeljak":
    print("Postavi boju na: crvenu")
elif dan_u_nedelji == "utorak":
    print("Postavi boju na: zelenu")
elif dan_u_nedelji == "sreda":
    print("Postavi boju na: zutu")
elif dan_u_nedelji == "cetvrtak":
    print("Postavi boju na: ljubicatu")
else:
    print("Postavi boju na belu.")

print("Izvrsava se u svakom slucaju")

broj = -5
# broj je veci od 0, broj je manji od 0 i broj je jednak nuli
if broj > 0:
    print("Broj je veci od 0")
elif broj == 0:
    print("Broj je jednak 0.")
else:
    print("Broj je manji od 0.")


pozicija_automobila = 0
pozicija_parkinga = 30
brzina = 10

# a                 p
pozicija_automobila += 10
print(pozicija_automobila)

if pozicija_automobila == pozicija_parkinga:
    print("Stigli ste na parking")
else:
    pozicija_automobila += brzina
    if pozicija_automobila == pozicija_parkinga:
        print("Stigli ste na parking!")
    else:
        pozicija_automobila += brzina
        if pozicija_automobila == pozicija_parkinga:
            print("Stigli ste na parking")   
        else: 
            pozicija_automobila += brzina
            # ...

print("Izvrsava se u svakom slucaju")

# dark / light tema
trenutna_tema_na_racunaru = "light"
# na sajtu primeni temu u skladu sa temom na racunaru korisnika

odabrana_tema_u_app = ""
# prva mogucnost
if trenutna_tema_na_racunaru == "light":
    odabrana_tema_u_app = "light"
else:
    odabrana_tema_u_app = "dark"
# druga mogucnost - ternarni operator
odabrana_tema_u_app = "light" if trenutna_tema_na_racunaru == "light" else "dark"

uneti_broj = int(input("Unesite broj: "))

if uneti_broj % 2 == 0:
    print("Broj je paran")
else:
    print("Broj je neparan")