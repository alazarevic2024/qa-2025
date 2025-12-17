public class BankAccountTests {

    public static void runAllTests() {
        testStartBalance();
        testDepositSuccess();
        testDepositInvalidZero();
    }

    /**
     * Ovaj unit test proverava inicijalno setovanje nvoca na racun
     */
    public static boolean testStartBalance() {
        double startBalance = 200;
        BankAccount bankAccount = new BankAccount(startBalance);

        double dobijeno = bankAccount.getBalance();
        if (dobijeno == startBalance) {
            System.out.println("PASS: start balance: "+dobijeno);
            return true;
        } else {
            System.out.println("FAIL: start balance: " + dobijeno
                    + "expected: " + startBalance);
            return false;
        }
    }

    public static boolean testDepositSuccess() {
        double pocetnoStanje = 2000;
        BankAccount bankAccount = new BankAccount(pocetnoStanje);
        double uplata = 500;
        double ocekivano = pocetnoStanje + uplata;

        bankAccount.deposit(uplata);
        double novoStanje = bankAccount.getBalance();
        if (novoStanje == ocekivano) {
            System.out.println("deposit - PASS: deposit successful: "+novoStanje);
            return true;
        } else {
            System.out.println("deposit - FAIL: excpected: "+ ocekivano +
                    "current balance: " + novoStanje);
            return false;
        }
    }

    public static boolean testDepositInvalidZero() {
        // Given
        double pocetnoStanje = 2000;
        BankAccount bankAccount = new BankAccount(pocetnoStanje);
        double uplata = 0;
        boolean ocekivano = false;
        double ocekivanoStanje = 2000;
        // When
        boolean uspesnaUplata = bankAccount.deposit(uplata);
        // Then
        double dobijenoStanje = bankAccount.getBalance();
        if (!uspesnaUplata && ocekivanoStanje == dobijenoStanje) {
            System.out.println("PASS: deposit invalid zero");
            return true;
        } else {
            System.out.println("FAIL: deposit invalid zero, expected : "
            + ocekivanoStanje + "dobijeno: " + dobijenoStanje );
            return false;
        }
    }

}
