class student2{
    String name;
    int marks;
    student2(){
        name="xyz";
        marks=85;
    }
    student2(String name){
        this.name=name;
        //this.marks=marks;
        marks=0;
    }   
    student2(String name, int marks){
        this.name=name;
        this.marks=marks;
    }
    void display(){
        System.out.println("name:"+name);
        System.out.println("marks:"+marks);
    }
}
public class constructo {
    public static void main(String[] args) {
        student2 s1=new student2();
        student2 s2=new student2("xyz");
        student2 s3=new student2("abc", 90);
        s1.display();
        s2.display();
        s3.display();
    }
}
