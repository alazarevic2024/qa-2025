def prikazi_rezultat_testa(naziv_testa, dobijeno, ocekivano):
    print("Test:",naziv_testa)
    print("Ocekivano:",ocekivano)
    print("Dobijeno:",dobijeno)
    print("Test prosao:", ocekivano == dobijeno)
    print("#######################################")

# Pravila obracuna dostave
# 0 - 1999 - 500 dinara 
# 2000 - 4999 - 300 dinara
# preko 5000 - besplatna dostava - 0 din
# negativan iznos - prikaz greske neispravan unos

def odredi_cenu_dostave(vrednost_porudzbine):
    if vrednost_porudzbine >= 0 and vrednost_porudzbine <= 1999:
        return 500
    elif vrednost_porudzbine >= 2000 and vrednost_porudzbine <= 4999:
        return 300
    elif vrednost_porudzbine >= 5000:
        return 0
    else:
        return "neispravan iznos"

def test_dostava_1000():
    vrednost = 1000
    ocekivana_dostava = 500
    dobijeno = odredi_cenu_dostave(vrednost)
    prikazi_rezultat_testa("Vrednost 1000", dobijeno, ocekivana_dostava)

def test_dostava_2000():
    vrednost = 2000
    ocekivana_dostava = 300
    dobijeno = odredi_cenu_dostave(vrednost)
    prikazi_rezultat_testa("Vrednost 2000", dobijeno, ocekivana_dostava)

def test_dostava_5000():
    vrednost_porudzbine = 5000
    ocekivana_dostava = 0
    dobijeno = odredi_cenu_dostave(vrednost_porudzbine)
    prikazi_rezultat_testa("Vrednost 5000", dobijeno, ocekivana_dostava)

def test_dostava_za_negativan_iznos():
    vrednost_porudzbine = -100
    ocekivano = "neispravan iznos"
    dobijeno = odredi_cenu_dostave(vrednost_porudzbine)
    prikazi_rezultat_testa("Negativna vrednost", dobijeno, ocekivano)

# test_dostava_1000()
# test_dostava_2000()
# test_dostava_5000()
# test_dostava_za_negativan_iznos()

'''
Proverili: 
1000 - 500
2000 - 300
5000 - 0
-100 - neispravan unos

Granice:
-1 , 0, 1999, 2000, 4999, 5000, 5001
----------------------
'''

def test_granicne_vrednosti_dostave():
    # vrednost | ocekivano
    test_podaci = [
        (-1,     "neispravan iznos"), 
        (0,      500), 
        (1999,   500), 
        (2000,   300),
        (4999,   300),
        (5000,   0),
        (5001,   0)
        ]
    
    for vrednost, ocekivano in test_podaci:
        dobijeno = odredi_cenu_dostave(vrednost)
        prikazi_rezultat_testa(f"Proveravamo granicnu vrednost: {vrednost}",dobijeno, ocekivano)

test_granicne_vrednosti_dostave()