public class PristupApp {

    /**
     * Metoda
     * Prihvata nivo (1, 2 ili 4) i vraca poruku sa pristupom ili gresku
     */
    public static String proveriPristup(int nivo) {
        boolean regular = false;
        boolean admin = false;
        boolean superAdmin = false;

        if (nivo == 1) {
            regular = true;
        } else if (nivo == 2) {
            regular = true;
            admin = true;
        } else if (nivo == 4) {
            regular = true;
            admin = true;
            superAdmin = true;
        } else {
            return "GRESKA: nivo mora biti 1, 2 ili 4";
        }
        // Regular: IMA ili NEMA
        // message = "IMA" if regular else "NEMA"
        return "Pristupi:\n"+"Regular: " +
                (regular ? "IMA" : "NEMA") + "\n" +
                "Admin: " + (admin ? "IMA" : "NEMA") + "\n" +
                "Superadmin: " + (superAdmin ? "IMA" : "NEMA");
    }

    /**
     * Automatski test za proveru vise ulaza
     */
    public static void pokreniTestove() {
        int[] testNivoi = {1, 2, 4, 0, 3, -1};

        for (int nivo: testNivoi) {
            System.out.println("Testiram nivo: "+nivo);
            System.out.println(proveriPristup(nivo));
        }
    }

}
