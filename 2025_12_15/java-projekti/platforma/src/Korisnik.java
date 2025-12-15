public class Korisnik {
    public String korisnickoIme;
    public String sifra;
    public String smer;
    public int godinaUpisa;
    public int krediti;
    private String jmbg;

    public final static String ustanova = "ITAcademy";

    public Korisnik(String korisnickoIme, String sifra, String smer, int godinaUpisa, int krediti) {
        this.korisnickoIme = korisnickoIme;
        this.sifra = sifra;
        this.smer = smer;
        this.godinaUpisa = godinaUpisa;
        this.krediti = krediti;
    }

    @Override
    public String toString() {
        return "Korisnik: " + korisnickoIme + " " + "smer " + smer;
    }

    public void promeniSmer(String noviSmer) {
        this.smer = noviSmer;
    }

    public void postaviJmbg(String jmbgKorisnika) {
        this.jmbg = jmbgKorisnika;
    }

    public String vratiJmbgMaskiran() {
        String deoZaPrikaz = this.jmbg.substring(jmbg.length() - 4);
        return "**********" + deoZaPrikaz;
    }

}
