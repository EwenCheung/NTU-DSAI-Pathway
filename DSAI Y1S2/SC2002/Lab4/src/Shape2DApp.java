import java.util.Scanner;

public class Shape2DApp {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the total number of shapes: ");
        int num = sc.nextInt();
        int i = 0;
        while (i < num) {
            System.out.println("Enter the shapes: ");
            System.out.println("1. Rectangle\n2. Square\n3. Triangle\n4. Circle");
            int shape = sc.nextInt();
            double area = 0;
            switch (shape) {
                case 1: {
                    System.out.print("Insert the length");
                    double length1 = sc.nextInt();
                    System.out.print("Insert the breadth");
                    double breadth1 = sc.nextInt();
                    Rectangle s1 = new Rectangle(length1, breadth1);
                    area = s1.findArea();
                    System.out.println("The area is"+area);
                    i++;
                    break;
                }

                case 2: {
                    System.out.print("Insert the length");
                    double length2 = sc.nextInt();
                    System.out.print("Insert the breadth");
                    double breadth2 = sc.nextInt();
                    Square s2 = new Square(length2, breadth2);
                    area = s2.findArea();
                    System.out.println("The area is"+area);
                    i++;
                    break;
                }

                case 3: {
                    System.out.print("Insert the height");
                    double height = sc.nextInt();
                    System.out.print("Insert the base");
                    double base = sc.nextInt();
                    Triangle s3 = new Triangle(height, base);
                    area = s3.findArea();
                    System.out.println("The area is"+area);
                    i++;
                    break;
                }

                case 4: {
                    System.out.print("Insert the radius");
                    double radius = sc.nextInt();
                    Circle s4 = new Circle(radius);
                    area = s4.findArea();
                    System.out.println("The area is"+area);
                    i++;
                    break;
                }

                default: {
                    System.out.println("Please enter number 1 - 4");
                }


            }
        }
    }
}

