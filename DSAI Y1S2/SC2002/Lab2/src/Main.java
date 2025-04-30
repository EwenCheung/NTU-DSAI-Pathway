import java.util.Scanner;
import java.util.Random;

public class Main {
    public static void main(String[] args) {

        int choice;
        Scanner sc = new Scanner(System.in);
        do {
            System.out.println("Perform the following methods:");
            System.out.println("1:multiplication test");
            System.out.println("2:quotient using division by subtraction");
            System.out.println("3:remainder using division by subtraction");
            System.out.println("4:count the number of digits");
            System.out.println("5:position of a digit");
            System.out.println("6:extract all odd digits");
            System.out.println("7:quit");
            choice = sc.nextInt();
            switch (choice) {
                case 1: /* add mulTest() call */
                    mulTest();
                    break;
                case 2: /* add divide() call */
                    System.out.print("m = ");
                    int m1 = sc.nextInt();
                    System.out.print("n = ");
                    int n1 = sc.nextInt();
                    int ans1 = divide(m1, n1);
                    System.out.println(m1 + " / " + n1 + " = " + ans1);
                    break;
                case 3: /* add modulus() call */
                    System.out.print("m =");
                    int m2 = sc.nextInt();
                    System.out.print("n = ");
                    int n2 = sc.nextInt();
                    int ans2 = modulus(m2, n2);
                    System.out.println(m2 + " % " + n2 + " = " + ans2);
                    break;
                case 4: /* add countDigits() call */
                    System.out.print("n = ");
                    int n3 = sc.nextInt();
                    int ans3 = countDigits(n3);
                    if (ans3 == -1) {
                        System.out.println("Error Input");
                    } else {
                        System.out.println("Count = " + ans3);
                    }
                    break;
                case 5: /* add position() call */
                    System.out.print("n = ");
                    int n4 = sc.nextInt();
                    System.out.print("What digit you want to find: ");
                    int dig = sc.nextInt();
                    int ans4 = position(n4, dig);
                    System.out.println("position = " + ans4);
                    break;
                case 6: /* add extractOddDigits() call */
                    System.out.print("n = ");
                    long n5 = sc.nextInt();
                    long ans5 = extractOddDigits(n5);
                    System.out.println("OddDigits = " + ans5);
                    break;
                case 7:
                    System.out.println("Program terminating ….");
                    break;
            }
        }
        while (choice < 7);
    }

    public static void mulTest() {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();
        int correct_count = 0;

        for (int i = 0; i < 5; i++) {
            int num1 = rand.nextInt(9) + 1;
            int num2 = rand.nextInt(9) + 1;
            System.out.println("How much is " + num1 + " times " + num2 + " ?");
            int ans = sc.nextInt();
            if (ans == num1 * num2) {
                correct_count++;
            }
        }

        System.out.println(correct_count + " answers out of 5 are correct.");
    }

    public static int divide(int m, int n) {
        int count = 0;
        while (m != 0 && m > (m - n)) {
            m = m - n;
            count++;
        }

        if (m != 0) {
            return 0;
        } else {
            return count;
        }
    }

    public static int modulus(int m, int n) {
        if (n==0){
            System.out.println("Error");
            return -1;
        }
        while (m >=n) {
            m = m - n;
        }
        return m;
    }

    public static int countDigits(int n) {
        int count = 0;
        if (n < 0) {
            return -1;
        }
        while (n > 0) {
            n /= 10;
            count++;
        }
        return count;
    }

    public static int position(int n, int digit) {
        int len = countDigits(n);
        int pos = -1;
        int count = 0;
        while (n > 0) {
            if (n % 10 == digit) {
                pos = len - count;
            }
            n /= 10;
            count++;
        }

        return pos;
    }

    public static long extractOddDigits(long n) {

        int count = 0;
        int odd = 0;
        while (n > 0) {
            if ((n % 10) % 2 == 1) {
                odd += (n % 10) * (Math.pow(10, count));
                count++;
            }
            n /= 10;

        }
        if (odd == 0) {
            return -1;
        }

        return odd;
    }

}