public class Book {
    private String title;
    private String author;
    private String genre;
    private int publicationYear;
    private String description;  // Optional field for search

    public Book(String title, String author, String genre, int publicationYear) {
        this(title, author, genre, publicationYear, "");
    }

    public Book(String title, String author, String genre, int publicationYear, String description) {
        this.title = title;
        this.author = author;
        this.genre = genre;
        this.publicationYear = publicationYear;
        this.description = description;
    }

    // Getters
    public String getTitle() {
        return title;
    }
    public String getAuthor() {
        return author;
    }
    public String getGenre() {
        return genre;
    }
    public int getPublicationYear() {
        return publicationYear;
    }
    public String getDescription() {
        return description;
    }

    @Override
    public String toString() {
        return String.format("{\"title\": \"%s\", \"author\": \"%s\", \"genre\": \"%s\", \"publicationYear\": %d}",
                title, author, genre, publicationYear);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        Book book = (Book) obj;
        return title.equals(book.title) && author.equals(book.author);
    }

    @Override
    public int hashCode() {
        return title.hashCode() + author.hashCode();
    }
}
