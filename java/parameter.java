class student1{
    String name;
    int marks;
    student1(String name, int marks){
        this.name=name;
        this.marks=marks;
    }
void display(){
    System.out.println("name:"+name);
    System.out.println("marks:"+marks);
}
}
public class parameter {
    public static void main(String[] args) {
        student1 s1=new student1("rohan", 85);
        s1.display();
    }
}