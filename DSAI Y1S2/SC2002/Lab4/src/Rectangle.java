
public class Rectangle {
    double length;
    double breadth;
    double height;

    public Rectangle(double length, double breadth){
        this.length = length;
        this.breadth = breadth;
    }

    public Rectangle(double length, double breadth,double height){
        this.length = length;
        this.breadth = breadth;
        this.height = height;
    }

    public double findArea() {
        return this.length * this.breadth;
    }

    public double findVolume(){
        return this.length * this.breadth*this.height;
    }

}
