import streamlit as st
import pickle

# --- Data Classes ---
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author} - Available: {self.is_available}"

    def issued(self):
        self.is_available = False

    def returned(self):
        self.is_available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        return self.books


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.issued_books = []

    def issue_book(self, book):
        if book.is_available:
            book.issued()
            self.issued_books.append(book)
            return f"Book '{book.title}' issued to {self.name}."
        else:
            return f"Book '{book.title}' is not available."

    def return_book(self, book):
        if book in self.issued_books:
            book.returned()
            self.issued_books.remove(book)
            return f"Book '{book.title}' returned by {self.name}."
        else:
            return f"You haven't issued book '{book.title}'."

# --- Data Load/Save ---
def save_data(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def load_data(filename):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except:
        return []

# --- Initialize ---
library = Library()
library.books = load_data("books.pkl")
users = load_data("users.pkl")

st.set_page_config(page_title="📚 Library System", layout="centered")
st.title("📚 Library Management System")
st.markdown("---")

menu = st.sidebar.selectbox("Choose Action", ["Add Book", "Display Books", "Register User", "Issue Book", "Return Book"])

if menu == "Add Book":
    st.header("➕ Add Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    isbn = st.text_input("ISBN")
    if st.button("Add"):
        book = Book(title, author, isbn)
        library.add_book(book)
        save_data("books.pkl", library.books)
        st.success("Book added successfully.")

elif menu == "Display Books":
    st.header("📚 Available Books")
    if library.books:
        for book in library.books:
            st.text(str(book))
    else:
        st.warning("No books available.")

elif menu == "Register User":
    st.header("👤 Register User")
    name = st.text_input("Name")
    user_id = st.text_input("User ID")
    if st.button("Register"):
        user = User(name, user_id)
        users.append(user)
        save_data("users.pkl", users)
        st.success(f"User {name} registered successfully.")

elif menu == "Issue Book":
    st.header("📖 Issue Book")
    user_id = st.text_input("User ID")
    title = st.text_input("Book Title")
    if st.button("Issue"):
        user = next((u for u in users if u.user_id == user_id), None)
        book = next((b for b in library.books if b.title == title), None)
        if not user:
            st.error("User not found.")
        elif not book:
            st.error("Book not found.")
        else:
            message = user.issue_book(book)
            save_data("books.pkl", library.books)
            save_data("users.pkl", users)
            st.info(message)

elif menu == "Return Book":
    st.header("↩ Return Book")
    user_id = st.text_input("User ID")
    title = st.text_input("Book Title")
    if st.button("Return"):
        user = next((u for u in users if u.user_id == user_id), None)
        book = next((b for b in library.books if b.title == title), None)
        if not user:
            st.error("User not found.")
        elif not book:
            st.error("Book not found.")
        else:
            message = user.return_book(book)
            save_data("books.pkl", library.books)
            save_data("users.pkl", users)
            st.info(message)

st.markdown("---")
st.write("Made with ❤️ by [MAHNOOR RAHEEL]")