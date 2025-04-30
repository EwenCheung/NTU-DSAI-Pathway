public class Triangle {
    double height;
    double base;
    double length;
    public Triangle(double height, double base){
        this.height = height;
        this.base = base;
    }

    public Triangle(double height, double base,double length){
        this.height = height;
        this.base = base;
        this.length = length;
    }

    public double findArea(){
        return (0.5*this.height*this.base);
    }

    public double findVolune(){

        return (0.5*this.height*this.base)*this.height;

    }

}
