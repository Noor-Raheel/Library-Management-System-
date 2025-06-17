# -------- Book Class --------
# Represents a single book in the library
class Book:
    def __init__(self, title, author, isbn):
        self.title = title               # Book title
        self.author = author             # Book author
        self.isbn = isbn                 # Book ISBN number
        self.is_available = True         # Book availability (default = True)

    def __str__(self):
        # String representation when we print(book)
        return f"{self.title} by {self.author} - Available: {self.is_available}"

    def issued(self):
        # Marks the book as issued (available = False)
        self.is_available = False

    def returned(self):
        # Marks the book as returned (available = True)
        self.is_available = True


# -------- Library Class --------
# Manages the collection of books
class Library:
    def __init__(self):
        self.books = []  # List to store all books in library

    def add_book(self, book):
        # Adds a book to the library
        self.books.append(book)

    def display_books(self):
        # Displays all books in the library
        for book in self.books:
            print(book)


# -------- User Class --------
# Represents a user who can borrow and return books
class User:
    def __init__(self, name, user_id):
        self.name = name                    # User name
        self.user_id = user_id              # Unique user ID
        self.issued_books = []              # List of books issued by user

    def issue_book(self, book):
        # Issue a book to the user if available
        if book.is_available:
            book.issued()                   # Call book's issued method
            self.issued_books.append(book)  # Add to user's issued list
            print(f"Book '{book.title}' issued to {self.name}.")
        else:
            print(f"Book '{book.title}' is not available.")  # Book already issued

    def return_book(self, book):
        # Return a book if the user has it
        if book in self.issued_books:
            book.returned()                 # Call book's return method
            self.issued_books.remove(book)  # Remove from user's issued list
            print(f"Book '{book.title}' returned by {self.name}.")
        else:
            print(f"You haven't issued book '{book.title}'.")  # Book not found with user


# -------- Main Program --------
library = Library()  # Create library object
users = []           # List to store all users

# Menu loop — keeps running until user exits
while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")          # Admin adds a book
    print("2. Display Books")     # View all books
    print("3. Register User")     # Create a new user
    print("4. Issue Book")        # Give book to user
    print("5. Return Book")       # User returns book
    print("6. Exit")              # End program

    choice = int(input("Enter your choice: "))

    # --- Option 1: Add Book ---
    if choice == 1:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        book = Book(title, author, isbn)    # Create book object
        library.add_book(book)              # Add to library
        print("Book added successfully.")

    # --- Option 2: Show all books ---
    elif choice == 2:
        library.display_books()

    # --- Option 3: Register a new user ---
    elif choice == 3:
        name = input("Enter user name: ")
        user_id = input("Enter user ID: ")
        user = User(name, user_id)         # Create new user
        users.append(user)                 # Add to user list
        print(f"User {name} registered.")

    # --- Option 4: Issue book to user ---
    elif choice == 4:
        user_id = input("Enter your user ID: ")
        title = input("Enter book title to issue: ")

        # Find user by ID
        user = next((u for u in users if u.user_id == user_id), None)
        if not user:
            print("User not found.")
            continue

        # Find book by title
        book = next((b for b in library.books if b.title == title), None)
        if not book:
            print("Book not found.")
            continue

        # Issue the book
        user.issue_book(book)

    # --- Option 5: Return book from user ---
    elif choice == 5:
        user_id = input("Enter your user ID: ")
        title = input("Enter book title to return: ")

        # Find user by ID
        user = next((u for u in users if u.user_id == user_id), None)
        if not user:
            print("User not found.")
            continue

        # Find book by title
        book = next((b for b in library.books if b.title == title), None)
        if not book:
            print("Book not found.")
            continue

        # Return the book
        user.return_book(book)

    # --- Option 6: Exit Program ---
    elif choice == 6:
        print("Goodbye!")
        break

    # --- Invalid Option ---
    else:
        print("Invalid choice. Try again.")

# --- End Program ---