//program to find sum of numbers using while loop
import java.util.Scanner;
    public class Q1total{
        public static void main(String[] args){
            Scanner sc=new Scanner(System.in);
                System.out.println("Enter a number");
                int number=sc.nextInt();
                    int total=0;
                    while (number!=0){
                        total=total+number;
                        System.out.println("Enter a number");
                        number=sc.nextInt();
                        System.out.println("------------");
                        System.out.println("Total: " + total);
                        System.out.println("------------");
                    }
                    System.out.println("-----------------");
                    System.out.println("New total:" + total);
                    System.out.println("-----------------");
                    sc.close();
            }    
    }