package com.codingfun;

import java.util.Scanner;

public class P1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Type a character: ");
        String character = scanner.next().toLowerCase();
        switch (character) {
            case "a":
                System.out.println("Action movie fan");
                break;
            case "c":
                System.out.println("Comedy movie fan");
                break;
            case "d":
                System.out.println();
                break;
            default:
                System.out.println("Invalid choice");


        }


        scanner.close();

    }
}