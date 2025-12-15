//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
void main() {
    /*
    int broj; // deklaracija
    broj = 10; // inicijalizacija
    String poruka = "Hello!"; // deklaracija i inicijalizacija
    System.out.println(poruka);
     */

    Korisnik korisnik1 = new Korisnik("Jovana", "123", "QA", 2025, 0);
    Korisnik korisnik2 = new Korisnik("Petar", "543", "QA", 2024, 0);
    Korisnik korisnik3 = new Korisnik("Marija", "111", "Python", 2025, 0);

    System.out.println(korisnik1.korisnickoIme);
    System.out.println(korisnik1.toString());

    // Obican niz korisnika - array
    Korisnik[] upisaniKorisniciNiz = {korisnik1, korisnik2, korisnik3};

    for (Korisnik korisnik : upisaniKorisniciNiz) {
        if (korisnik.godinaUpisa == 2025 && korisnik.smer.equals("QA")) {
            System.out.println("Ocekivano - QA - 2025");
        } else {
            System.out.println("Greska - korisnik je smer: " + korisnik.smer + " i godina upisa je: "
                    + korisnik.godinaUpisa);
        }
    }

    // Naknadno dodajem
    ArrayList<Korisnik> listaKorisnika = new ArrayList<>();
    listaKorisnika.add(korisnik1);
    listaKorisnika.add(korisnik2);
    listaKorisnika.add(korisnik3);

    // Odmah dodajem
    ArrayList<Korisnik> listaKorisnikaQA = new ArrayList<>(List.of(korisnik1, korisnik2, korisnik3));

    for (int i = 0; i < listaKorisnikaQA.size(); i++) {
        System.out.println(listaKorisnikaQA.get(i));
    }

    korisnik1.promeniSmer("Python");
    System.out.println(korisnik1.smer);

    korisnik1.postaviJmbg("123456789");
//    System.out.println(korisnik1.jmbg); ovo ne moze jer je private - koristi getter metodu
    System.out.println(korisnik1.vratiJmbgMaskiran());

}
