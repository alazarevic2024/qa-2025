public class UslugaOglas extends Oglas {
    private int hourlyRate;

    public UslugaOglas(String title, String owner, int hourlyRate) {
        super(title, owner);
        this.hourlyRate = hourlyRate;
    }
}
