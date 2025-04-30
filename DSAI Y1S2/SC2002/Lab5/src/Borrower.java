import java.util.ArrayList;
import java.util.List;

public class Borrower {
    private String name;
    private List<Book> borrowedBooks;

    public Borrower(String name) {
        this.name = name;
        this.borrowedBooks = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public List<Book> getBorrowedBooks() {
        return borrowedBooks;
    }

    // Borrow a book if it's available in the library and not already borrowed
    public void borrowBook(Book book, Library library) {
        if (library.getBooks().contains(book) && !borrowedBooks.contains(book)) {
            borrowedBooks.add(book);
            System.out.println("\nBook borrowed: " + book.getTitle());
        } else {
            System.out.println("Book not available or already borrowed.");
        }
    }

    // Return a borrowed book
    public void returnBook(Book book) {
        if (borrowedBooks.remove(book)) {
            System.out.println("\nBook returned: " + book.getTitle());
        } else {
            System.out.println("This book was not borrowed.");
        }
    }

    @Override
    public String toString() {
        return "Borrower: " + name + ", Borrowed Books: " + borrowedBooks;
    }
}
