class student{
    student(){
        System.out.println("called constructor");
    }
}
public class new1 {
    public static void main(String[] args) {
        student s1=new student();
        System.out.println("program finished");
        System.out.println(s1);
    }
}

