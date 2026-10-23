class HRsystem{
    private String name;
    private int employeeid;
    private double salary;

    HRsystem(String name) {
        this.name = name;
    }

    HRsystem(String name, int employeeid) {
        this.name = name;
        this.employeeid = employeeid;
    }
    HRsystem(String name, int employeeid, double salary) {
        this.name = name;
        this.employeeid = employeeid;
        this.salary = salary;
    }

    void display() {
        System.out.println("Name: "+name);
        System.out.println("Employee ID:"+ employeeid);
        System.out.println("Salary:"+ salary);
    }
}
public class HRsyste {
    public static void main(String[] args) {
        HRsystem hr1 = new HRsystem("rahul", 3054, 50000);
        HRsystem hr2 = new HRsystem("abc", 3589, 60000);
        HRsystem hr3 = new HRsystem("xyz", 4065, 70000);
        hr1.display();
        hr2.display();
        hr3.display();
    }
}
