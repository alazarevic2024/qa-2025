# funkcija za sabiranje brojeva
def test_saberi_dva_broja():
    ocekivano = 5
    dobijeno = saberi(2,3)
    print("Prosao:", ocekivano == dobijeno)

def saberi(a,b):
    return a+b

test_saberi_dva_broja()