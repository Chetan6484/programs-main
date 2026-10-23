class bankaccount{
    private int accountnumber;
    private String holdername;
    private double balance;
    
    void setaccountnumber(int accountnumber){
        this.accountnumber=accountnumber;
    }
    void setholdername(String holdername){
        this.holdername=holdername;
    }
    void setbalance(double balance){
        if(balance >= 0) {
            this.balance=balance;
        }else{
            System.out.println("invalid balance");
        }
    }

    int getaccountnumber(){
    return accountnumber;
    }
    String getholdername(){
        return holdername;
    }
    double getbalance(){
        return balance;
    }
}
    public class bank{
        public static void main(String [] args){
    bankaccount b1=new bankaccount();
    b1.setaccountnumber(12345);
    System.out.println(b1.getaccountnumber());
    b1.setholdername("John Doe");
    System.out.println(b1.getholdername());
    b1.setbalance(1000.50);
    System.out.println(b1.getbalance());
}
}

