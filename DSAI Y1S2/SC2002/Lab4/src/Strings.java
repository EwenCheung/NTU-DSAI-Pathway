import java.util.Scanner;

import java.util.Scanner;
public class Strings
{
    // --------------------------------------------
// Reads in an array of integers, sorts them,
// then prints them in sorted order.
// --------------------------------------------
    public static void main (String[] args)
    {
        String[] strList;
        int size;
        Scanner scan = new Scanner(System.in);
        System.out.print ("\nHow many words do you want to sort? ");
        size = scan.nextInt();
        strList = new String[size];
        System.out.println ("\nEnter the word...");
        for (int i = 0; i < size; i++)
            strList[i] = scan.next();
//        Sorting.selectionSort(strList);
        Sorting.insertionSort(strList);
        System.out.println ("\nYour words in sorted order...");
        for (int i = 0; i < size; i++)
            System.out.print(strList[i] + " ");
        System.out.println ();
    }
}