package com.codingfun;

import java.util.Scanner;

public class P2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your salary");
        double salary = scanner.nextDouble();
        System.out.print("Enter your merit");
        int merit = scanner.nextInt();
        String grade = "";

        if (500 <= salary && salary <= 600) {
            grade = "C";
        } else if (649 < salary && salary < 700) {
            grade = "B";
        } else if (799 < salary && salary <= 899) {
            grade = "A";
        } else if (600 <= salary && salary <= 649) {
            if (merit < 10) {
                grade = "C";

            } else {
                grade = "B";

            }
        } else if (700 <= salary && salary <= 799) {
            if (merit < 20) {
                grade = "B";
            } else {
                grade = "A";
            }
        }
        System.out.println(grade);
        scanner.close();

    }
}
