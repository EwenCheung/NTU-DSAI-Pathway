import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class LibraryApp {
    public static void main(String[] args) {
        Library library = new Library();

        // Test Case 1: Adding Books to the Library
        Book book1 = new Book("1984", "George Orwell", "Fiction", 1949, "A dystopian novel.");
        Book book2 = new Book("A Brief History of Time", "Stephen Hawking", "Science", 1988, "An overview of cosmology.");
        library.addBook(book1);
        library.addBook(book2);
        System.out.println("Library contains " + library.getBooks().size() + " books.");

        // Test Case 2: Filtering Books by Genre
        System.out.println("\nFiltering by genre 'Fiction':");
        List<Book> fictionBooks = library.filterByGenre("Fiction");
        fictionBooks.forEach(System.out::println);

        // Test Case 3: Filtering Books by Author
        System.out.println("\nFiltering by author 'Stephen Hawking':");
        List<Book> hawkingBooks = library.filterByAuthor("Stephen Hawking");
        hawkingBooks.forEach(System.out::println);

        // Test Case 4: Searching Books by Keyword "Time"
        System.out.println("\nSearching for books with keyword 'Time':");
        List<Book> searchedBooks = library.searchBooks("Time");
        searchedBooks.forEach(System.out::println);

        // Test Case 5: Adding another book and sorting by title
        Book book3 = new Book("A Beautiful Mind", "Sylvia Nasar", "Biography", 1998, "The life of John Nash.");
        library.addBook(book3);

        List<Book> sortedBooks = library.getBooks().stream()
                .sorted(Comparator.comparing(Book::getTitle))
                .collect(Collectors.toList());
        System.out.println("\nBooks sorted by title:");
        sortedBooks.forEach(book -> System.out.println(book.getTitle()));

        // Test Case 6: Providing Recommendations
        System.out.println("\nRecommendation for Science category:");
        System.out.println(library.recommendBook("Science"));

        // Test Case 7: Borrower Operations
        Borrower alice = new Borrower("Alice");
        alice.borrowBook(book1, library);  // Borrowing "1984"
        System.out.println(alice);

        // Test Case 8: Returning a Book
        alice.returnBook(book1);
        System.out.println(alice);
    }
}
