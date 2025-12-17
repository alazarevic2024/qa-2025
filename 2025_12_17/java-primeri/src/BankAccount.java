public class BankAccount {

    private double balance;

    public BankAccount(double startBalance) {
        if (startBalance >= 0) {
            this.balance = startBalance;
        }
    }

    /**
    Vraca stanje na racunu - balance
     */
    public double getBalance() {
        return balance;
    }

    /**
     * Unosi vrednost na racun
     */
    public boolean deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            return true;
        }
        return false;
    }

    /**
     * Preuzimanje novca sa racuna
     */
    public boolean withdraw(double amount) {
        if (amount > 0 && balance >= amount) {
            balance -= amount;
            return true;
        }
        return false;
    }
}
