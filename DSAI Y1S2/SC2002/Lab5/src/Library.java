import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class Library {
    private List<Book> books;

    public Library() {
        books = new ArrayList<>();
    }

    // Adds a book to the library
    public void addBook(Book book) {
        books.add(book);
    }

    // Removes a book from the library
    public void removeBook(Book book) {
        books.remove(book);
    }

    // Returns all books in the library
    public List<Book> getBooks() {
        return books;
    }

    // Filters books by genre using a stream and lambda expression
    public List<Book> filterByGenre(String genre) {
        return books.stream()
                .filter(b -> b.getGenre().equalsIgnoreCase(genre))
                .collect(Collectors.toList());
    }

    // Filters books by author using a stream and lambda expression
    public List<Book> filterByAuthor(String author) {
        return books.stream()
                .filter(b -> b.getAuthor().equalsIgnoreCase(author))
                .collect(Collectors.toList());
    }

    // Searches books by keyword in the title or description
    public List<Book> searchBooks(String keyword) {
        return books.stream()
                .filter(b -> b.getTitle().toLowerCase().contains(keyword.toLowerCase()) ||
                        b.getDescription().toLowerCase().contains(keyword.toLowerCase()))
                .collect(Collectors.toList());
    }

    // Provides a recommendation based on genre (category)
    public String recommendBook(String category) {
        List<Book> filtered = books.stream()
                .filter(b -> b.getGenre().equalsIgnoreCase(category))
                .collect(Collectors.toList());
        if (!filtered.isEmpty()) {
            // For simplicity, recommend the first book found.
            Book rec = filtered.get(0);
            return "Try '" + rec.getTitle() + "' by " + rec.getAuthor() + ".";
        } else {
            return "No recommendation available for category " + category;
        }
    }
}
