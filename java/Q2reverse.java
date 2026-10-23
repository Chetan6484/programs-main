//program to reverse a number take integer from user takeinput from user
import java.util.Scanner;
    public class Q2reverse{
        public static void main(String[] args){
            Scanner sc=new Scanner(System.in);
                System.out.println("Enter a number");
                int number=sc.nextInt();
                    int reverse=0;
                    while (number!=0){
                        int digit=number%10;
                        reverse=reverse*10+digit;
                        number=number/10;
                    }
                    System.out.println("Reverse of the number is:"+reverse);
                    sc.close();
            }    
    }