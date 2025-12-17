public class Oglas {

    String title;
    String owner;

    public Oglas(String title, String owner) {
        this.title = title;
        this.owner = owner;
    }

    public String details() {
        return "Oglas: " + this.title + "\n" + "Owner: " + this.owner;
        //return String.format("Oglas: %s; Owner: %s", this.title, this.owner);
    }
}
