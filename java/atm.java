//program for atm 
import java.util.Scanner;

public class atm {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int choice;
        double balance = 5000;
        double amount;

        do {

        
            System.out.println("1. Check Balance");
            System.out.println("2. Deposit");
            System.out.println("3. Withdraw");
            System.out.println("4. Exit");

            System.out.println("Enter choice: ");
            choice = sc.nextInt();

            switch (choice) {

                case 1:
                    System.out.println("Balance = " + balance);
                    break;

                case 2:
                    System.out.println("Enter deposit amount: ");
                    amount = sc.nextDouble();

                    if (amount > 0) {
                        balance = balance + amount;
                        System.out.println("Amount deposited successfully");
                        System.out.println("Balance = " + balance);
                    } else {
                        System.out.println("Invalid amount");
                    }
                    break;

                case 3:
                    System.out.println("Enter withdraw amount: ");
                    amount = sc.nextDouble();

                    if (amount > 0 && amount <= balance) {
                        balance = balance - amount;
                        System.out.println("Please collect your cash");
                        System.out.println("Balance = " + balance);
                    } else {
                        System.out.println("Insufficient balance or invalid amount");
                    }
                    break;

                case 4:
                    System.out.println("Thank you ");
                    break;

                default:
                    System.out.println("Invalid choice");
            }

        } while (choice != 4);

        sc.close();
    }
}