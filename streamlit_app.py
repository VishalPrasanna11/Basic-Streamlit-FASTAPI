# Streamlit Frontend (app.py)
import streamlit as st
import requests
import pandas as pd
import os

# Configuration
API_URL = os.getenv('API_URL', 'http://localhost:8000')

def main():
    st.title("Online Bookshop")
    
    # Sidebar menu
    menu = st.sidebar.selectbox(
        "Menu",
        ["View Books", "Add Book", "Search Book"]
    )
    
    if menu == "View Books":
        show_books()
    elif menu == "Add Book":
        add_book()
    else:
        search_book()

def show_books():
    st.header("Available Books")
    
    # Fetch books from API
    response = requests.get(f"{API_URL}/books/")
    if response.status_code == 200:
        books = response.json()
        df = pd.DataFrame(books)
        st.dataframe(df)
    else:
        st.error("Failed to fetch books")

def add_book():
    st.header("Add New Book")
    
    # Book input form
    with st.form("add_book_form"):
        book_id = st.number_input("Book ID", min_value=1, step=1)
        title = st.text_input("Title")
        author = st.text_input("Author")
        price = st.number_input("Price", min_value=0.0, step=0.01)
        stock = st.number_input("Stock", min_value=0, step=1)
        
        if st.form_submit_button("Add Book"):
            book_data = {
                "id": book_id,
                "title": title,
                "author": author,
                "price": price,
                "stock": stock
            }
            
            response = requests.post(f"{API_URL}/books/", json=book_data)
            if response.status_code == 200:
                st.success("Book added successfully!")
            else:
                st.error(f"Failed to add book: {response.json()['detail']}")

def search_book():
    st.header("Search Book")
    
    book_id = st.number_input("Enter Book ID", min_value=1, step=1)
    if st.button("Search"):
        response = requests.get(f"{API_URL}/books/{book_id}")
        if response.status_code == 200:
            book = response.json()
            st.json(book)
        else:
            st.error("Book not found")

if __name__ == "__main__":
    main()