public class Circle {
    double radius;
    double height;

    public Circle(double radius){
        this.radius = radius;
    }

    public Circle(double radius, double height){
        this.radius = radius;
        this.height = height;
    }

    public double findArea(){
        return 3.1415926*(Math.pow(this.radius,2));
    }

    public double findVolume(){
        return 3.1415926*(Math.pow(this.radius,2))*this.height;
    }
}
