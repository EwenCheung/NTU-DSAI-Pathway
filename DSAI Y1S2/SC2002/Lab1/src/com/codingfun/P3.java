package com.codingfun;

import java.util.Scanner;

public class P3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Starting: ");
        double start = scanner.nextDouble();
        System.out.print("Ending");
        double end = scanner.nextDouble();
        System.out.print("Increment");
        double increment = scanner.nextDouble();

        if (end < start){
            System.out.println("Invalid input, ending must be larger than starting");
            scanner.close();
            return;
        }

        System.out.printf("%-10s %-10s%n", "US$", "S$");
        System.out.println("------------");
        for (double i = start; i <= end; i += increment) {
            System.out.printf("%-10s %-10s%n", i, i * 1.82);
        }
        System.out.println("\n");

        double i = start;
        System.out.printf("%-10s %-10s%n", "US$", "S$");
        System.out.println("------------");
        while (i <= end) {
            System.out.printf("%-10s %-10s%n", i, i * 1.82);
            i += increment;
        }
        System.out.println("\n");

        i = start;
        System.out.printf("%-10s %-10s%n", "US$", "S$");
        System.out.println("------------");
        do {
            System.out.printf("%-10s %-10s%n", i, i * 1.82);
            i += increment;
        } while (i <= end);

        scanner.close();
    }
}
