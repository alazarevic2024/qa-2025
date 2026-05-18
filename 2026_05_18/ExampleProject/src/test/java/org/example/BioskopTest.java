package org.example;

import org.junit.Assert;
import org.junit.Test;

public class BioskopTest {

    @Test
    public void izracnuajCenuZaObicnuKartu() {
        Bioskop bioskop = new Bioskop();
        double cena = bioskop.izracunajCenuKarte(false, false, false);
        double ocekivano = 600;

        Assert.assertEquals(ocekivano, cena, 0);
    }

}
