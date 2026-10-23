//take 10 number from the user and print only positive numbers using continue
import java.util.Scanner;
class Q5positive{
    public static void main(String[]args){
        Scanner sc =new Scanner(System.in);
        int count=0;
        while (count<10) {
            System.out.println("Enter a number:");
            int num=sc.nextInt();
            count++;
            if (num<0) {
                continue;
            }
            System.out.println("positive no is"+num);
        }
        sc.close();
    }
}

