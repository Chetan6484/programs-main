import java.util.Scanner;
public class Q3palindrome {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.println("enter a number");
        int num=sc.nextInt();
        int original_num=num;
        int reverse_num=0;
        while(num!=0){
            int num1=num%10;
            reverse_num=reverse_num*10+num1;
            num=num/10;
        }
        if(original_num==reverse_num){
            System.out.println(original_num+" is a palindrome");
        }
        else{
            System.out.println(original_num+" is not a palindrome");
        }
        sc.close();
    }
}
