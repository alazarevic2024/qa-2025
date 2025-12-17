public class ProdajaOglas extends Oglas {

    private String condition;

    public ProdajaOglas(String title, String owner, String condition) {
        super(title, owner);
        this.condition = condition;
    }

    @Override
    public String details() {
        super.details();
        return "Ovo je oglas za prodaju!";
    }
}
