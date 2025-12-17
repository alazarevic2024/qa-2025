////TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
//// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
void main() {

    // Regular 1, Admin 2, Superadmin 4
//    String rezultat = PristupApp.proveriPristup(4);
//    System.out.println(rezultat);

//    PristupApp.pokreniTestove();

    BankAccount racun = new BankAccount(500);
    BankAccount racun2 = new BankAccount(400);

//    System.out.println(racun.balance); ne moze jer je private

    System.out.println(racun.getBalance());
    System.out.println(racun2.getBalance());

    System.out.println(racun.deposit(500));
    System.out.println(racun.getBalance());

    racun.withdraw(300);
    System.out.println(racun.getBalance());

    Dog dog = new Dog(); // jedan pas
    Cat cat = new Cat(); // macka

    dog.sound();
    cat.sound();

    BankAccountTests.runAllTests();

}

