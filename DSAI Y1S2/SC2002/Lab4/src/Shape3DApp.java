import java.util.Scanner;

public class Shape3DApp {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the total number of shapes: ");
        int num = sc.nextInt();
        int i = 0;

        while (i < num) {
            System.out.println("\nChoose a shape: ");
            System.out.println("1. Rectangle\n2. Square\n3. Triangle\n4. Circle");
            int shape = sc.nextInt();
            double output = 0;

            switch (shape) {
                case 1: // Rectangle
                    System.out.print("Find:\n1. Area\n2. Volume\nChoose: ");
                    int chooseRect = sc.nextInt();

                    System.out.print("Insert the length: ");
                    double lengthR = sc.nextDouble();
                    System.out.print("Insert the breadth: ");
                    double breadthR = sc.nextDouble();

                    if (chooseRect == 1) { // Area
                        Rectangle rect = new Rectangle(lengthR, breadthR);
                        output = rect.findArea();
                    } else { // Volume
                        System.out.print("Insert the height: ");
                        double heightR = sc.nextDouble();
                        Rectangle rect = new Rectangle(lengthR, breadthR, heightR);
                        output = rect.findVolume();
                    }
                    break;

                case 2: // Square
                    System.out.print("Find:\n1. Area\n2. Volume\nChoose: ");
                    int chooseSquare = sc.nextInt();

                    System.out.print("Insert the side length: ");
                    double side = sc.nextDouble();

                    if (chooseSquare == 1) { // Area
                        Square square = new Square(side, side);
                        output = square.findArea();
                    } else { // Volume
                        System.out.print("Insert the height: ");
                        double heightS = sc.nextDouble();
                        Square square = new Square(side, side, heightS);
                        output = square.findVolume();
                    }
                    break;

                case 3: // Triangle
                    System.out.print("Find:\n1. Area\n2. Volume\nChoose: ");
                    int chooseTriangle = sc.nextInt();

                    System.out.print("Insert the height: ");
                    double heightT = sc.nextDouble();
                    System.out.print("Insert the base: ");
                    double baseT = sc.nextDouble();

                    if (chooseTriangle == 1) { // Area
                        Triangle triangle = new Triangle(heightT, baseT);
                        output = triangle.findArea();
                    } else { // Volume
                        System.out.print("Insert the length: ");
                        double lengthT = sc.nextDouble();
                        Triangle triangle = new Triangle(heightT, baseT, lengthT);
                        output = triangle.findVolune();
                    }
                    break;

                case 4: // Circle
                    System.out.print("Find:\n1. Area\n2. Volume\nChoose: ");
                    int chooseCircle = sc.nextInt();

                    System.out.print("Insert the radius: ");
                    double radius = sc.nextDouble();

                    if (chooseCircle == 1) { // Area
                        Circle circle = new Circle(radius);
                        output = circle.findArea();
                    } else { // Volume
                        System.out.print("Insert the height: ");
                        double heightC = sc.nextDouble();
                        Circle circle = new Circle(radius, heightC);
                        output = circle.findVolume();
                    }
                    break;

                default:
                    System.out.println("Invalid input. Please enter a number between 1 - 4.");
                    continue; // Skip this iteration and ask again
            }

            System.out.println("The output is: " + output);
            i++;
        }

        sc.close();
    }
}
