class student{
    String name;
    int marks;
student(){
    name="unknown";
    marks=0;
}
void display(){
    System.out.println("name:"+name);
    System.out.println("marks:"+marks);
}
public class argumen {
    public static void main(String[] args) {
        student s1=new student();
        s1.display();
    }
}
}
