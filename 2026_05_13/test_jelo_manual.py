import jelo as j
from jelo import Jelo

def test_promeni_cenu():
    # Given / Arrange
    pizza = Jelo("Pizza", 500)
    print("Pocetna cena:", pizza.cena)

    # When / Act
    pizza.promeni_cenu(900)

    # Then / Assert
    assert pizza.cena == 900

def test_dodaj_porez():
    # Given
    jelo = Jelo("Pasta", 1000)
    # When
    jelo.dodaj_porez(20)
    # Then
    assert jelo.cena == 1200

test_promeni_cenu()
test_dodaj_porez()