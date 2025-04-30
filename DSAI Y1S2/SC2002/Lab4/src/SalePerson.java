public class SalePerson implements Comparable{
    private String firstName;
    private String lastName;
    private int totalSales;

    public SalePerson (String firstName,String lastName, int totalSales){
        this.firstName = firstName;
        this.lastName = lastName;
        this.totalSales = totalSales;
    }

    public String toString() {
        return lastName+","+firstName+":"+totalSales;
    }

    public boolean equals(Object o){
        return ((SalePerson)o).firstName == ((SalePerson)o).lastName;
    }

    public int compareTo(Object o){
        if (this.getTotalSales() < ((SalePerson)o).getTotalSales()){
            return -1;
        }
        else if (this.getTotalSales() > ((SalePerson)o).getTotalSales()){
            return 1;
        }
        else{
            if ((this.getLastName().charAt(0) < ((SalePerson)o).getLastName().charAt(0))){
                return 1;
            }
            else{
                return -1;
            }
        }
    }

    public String getFirstName(){
        return this.firstName;
    }
    public String getLastName(){
        return this.lastName;
    }
    public int getTotalSales(){
        return this.totalSales;
    }
}
