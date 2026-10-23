//program to take 10 numbers from the user if the user enters 50 stop taking further number
import java.util.Scanner;
public class Q4num {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int count=0;
        while (count<10) {
            System.out.println("Enter a number:");
            int num=sc.nextInt();
            if (num>=50) {
                break;
            }
            count++;
        }
        sc.close();
    }
}