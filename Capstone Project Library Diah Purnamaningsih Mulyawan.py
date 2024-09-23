book = {
    1001: {
        "book_name": "The Little Prince",
        "author": "Antoine",
        "year_released": 1943,
        "genre": "Fiction",
        "stock": 2,
        "status": "Available"
    },
    1002: {
        "book_name": "Harry Potter",
        "author": "J. K. Rowling",
        "year_released": 1997,
        "genre": "Fiction",
        "stock": 2,
        "status": "Available"
    },
    1003: {
        "book_name": "The Hobbit",
        "author": "J. R. R. Tolkien",
        "year_released": 1937,
        "genre": "Fiction",
        "stock": 2,
        "status": "Available"
    },
    1004: {
        "book_name": "The Hunger Games",
        "author": "Suzanne Collins",
        "year_released": 2008,
        "genre": "Fiction",
        "stock": 2,
        "status": "Available"
    },
    1005: {
        "book_name": "Dune",
        "author": "Frank Herbert",
        "year_released": 1965,
        "genre": "Fiction",
        "stock": 2,
        "status": "Available" 
    },
    1006: {
        "book_name": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year_released": 1925,
        "genre": "Fiction",
        "stock": 2,
        "status": "Available"
    },
    1007: {
        "book_name": "Alexander Hamilton",
        "author": "Ron Chernow",
        "year_released": 2004,
        "genre": "Non Fiction",
        "stock": 2,
        "status": "Available"
    },
    1008: {
        "book_name": "1776",
        "author": "David McCullough",
        "year_released": 2005,
        "genre": "Non Fiction",
        "stock": 2,
        "status": "Available"
    },
    1009: {
        "book_name": "Atomic Habits",
        "author": "James CLeare",
        "year_released": 2018,
        "genre": "Non Fiction",
        "stock": 2,
        "status": "Available"
    },
    1010: {
        "book_name": "How to Win Friends",
        "author": "Dale Carnegie",
        "year_released": 1936,
        "genre": "Non Fiction",
        "stock": 2,
        "status": "Available"
    },
}


def login(): # Login admin
    
    correct_username = "admin"
    correct_password = "admin"
    
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if username == correct_username and password == correct_password:
            print("\nLogin successful! Welcome to BorrowBook\n ")
            main_menu()

        else:
            print("\nInvalid password. Please try again.\n")


def main_menu(): # Main Menu
    while True:
        print("\n=== Main Menu ===\n")
        print("1. Show All Book")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Add New Book")
        print("5. Edit Book Data")
        print("6. Delete Book")
        print("7. Exit Menu")

        menu = int(input("Please select the Menu: "))

        if menu == 1:
            show_all_books()
        elif menu == 2:
            borrow_book()
        elif menu == 3:
            return_book()
        elif menu == 4:
            add_book()
        elif menu == 5:
            edit_book()
        elif menu == 6:
            delete_book()
        elif menu == 7:
            print("Thank you for visiting BorrowBook.")
            break
        else:
            print("Invalid option. Please try again.")

def update_status(book_id):
    if book[book_id]['stock'] < 1:
        book[book_id]['status'] = "Not Available"
    else:
        book[book_id]['status'] = "Available"

def show_all_books(): # Menu 1: Show All Book (READ)
    print("\n\n=== All Books ===\n")
    print(f"{'ID':<5} | {'Book Name':<20} | {'Author':<20} | {'Genre':<12} | {'Year Released':<14} | {'Stock':<6} | {'Status':<14}")
    for book_id in book:
        update_status(book_id)
        book_info = book[book_id]
        print(f"{book_id:<5} | {book_info['book_name']:<20} | {book_info['author']:<20} | {book_info['genre']:<12} | {book_info['year_released']:<14} | {book_info['stock']:<6} | {book_info['status']:<14}")
    input("\nEnter to return to Main Menu.")
    main_menu()

def borrow_book(): # Menu 2: Borrow a Book (UPDATE)
    while True:
        print("\n=== Select Genre ===\n")
        print("1. Fiction")
        print("2. Non Fiction")
        print("3. Back to Main Menu")

        genre = int(input("Please select the Genre: "))

        if genre == 1:
            select_genre(book, "Fiction")
        elif genre == 2:
            select_genre(book, "Non Fiction")
        elif genre == 3:
            main_menu()
            return
        else:
            print("Invalid option. Please try again.")

def filter_books_by_genre(genre):
    def filter_function(book_item):
        _, book_info = book_item
        return book_info['genre'] == genre
    return filter_function

def select_genre(book, genre):
    filtered_books = filter(filter_books_by_genre(genre), book.items())
    print(f"\n=== Books in '{genre}' Genre ===\n")
    print(f"{'ID':<5} | {'Book Name':<20} | {'Author':<21} | {'Status':<15}")
    for book_id, book_info in filtered_books:
        print(f"{book_id:<5} | {book_info['book_name']:<20} | {book_info['author']:<21} | {book_info['status']:<15}")

    choice = input("\nWanna borrow a book? (yes/no) ").strip().lower()

    if choice == "yes":
        rent_book()
    elif choice == "no":
        borrow_book()
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

def rent_book():
    total_cost = 0
    receipt = []

    while True:
        borrow_book_id = input("Enter Book ID to borrow (or press Enter to finish): ")
        if borrow_book_id.lower() == "":
            break

        if borrow_book_id.isdigit():
            borrow_book_id = int(borrow_book_id)

        if borrow_book_id in book:
            book_info = book[borrow_book_id]
            qty_book = int(input(f"Enter qty for '{book_info['book_name']}': "))
            
            if qty_book <= book_info['stock']:
                book_info['stock'] -= qty_book
                total_cost += qty_book * 5000   # rent cost per book
                receipt.append((borrow_book_id, book_info['book_name'], qty_book, qty_book * 5000))
                print(f"Successfully borrowed '{book_info['book_name']}'")
            else:
                print(f"Not enough stock for '{book_info['book_name']}'.")
        else:
            print(f"Invalid book ID. Please try again.")

    print_receipt(receipt, total_cost)

def print_receipt(receipt, total_cost):
    print("\n=== Receipt ===\n")
    print(f"{'Book ID':<8} | {'Book Name':<20} | {'Quantity':<10} | {'Total Cost':<10}")

    for book_id, book_name, qty, cost in receipt:
        print(f"{book_id:<8} | {book_name:<20} | {qty:<10} | IDR {cost:<10}")

    print(f"\n{'Total Cost':<38} : IDR {total_cost}\n")
    print("Thank you for borrowing from BorrowBook!")
    input("\nEnter to return to Main Menu.")
    main_menu()

def return_book():  # Menu 3: Return Book (UPDATE)
    print("\n=== Return Book ===\n")

    book_id = input("Enter Book ID to return: ")

    if book_id.isdigit():
        book_id = int(book_id)

        if book_id in book:
            qty_return = int(input(f"Enter qty for return: "))

            if qty_return > 0:
                max_stock = 2
                if book[book_id]['stock'] + qty_return <= max_stock:
                    book[book_id]['stock'] += qty_return
                    book[book_id]['status'] = "Available" if book[book_id]['stock'] > 0 else "Not Available"
                    print(f"You have returned {qty_return} pcs of '{book[book_id]['book_name']}'. Thank you!")
                else:
                    print("You cannot return more than the available stock.")
            else:
                print("Please enter a correct amount.")
        else:
            print("Book ID not found. No books were returned.")
    else:
        print("Invalid book ID. Please try again.")

    input("\nEnter to return to Main Menu.")
    main_menu()

def add_book(): # Menu 4: Add Book (CREATE)
    print("\n=== Add New Book ===\n")
    
    book_id = int(input("Enter new book ID: "))
    if book_id in book:
        print("A book with this ID already exists.")
        return
    
    book_name = input("Enter book name: ")
    author = input("Enter author name: ")
    year_released = int(input("Enter year released: "))
    genre = input("Enter genre: ")
    stock = int(input("Enter stock quantity: "))
    
    book[book_id] = {
        "book_name": book_name,
        "author": author,
        "year_released": year_released,
        "genre": genre,
        "stock": stock,
        "status": "Available"
    }
    
    print(f"Book '{book_name}' has been added.")

    input("\nEnter to return to Main Menu.")
    main_menu()

def edit_book():  # Menu 5: Edit Book Data (UPDATE)
    while True:
        print("\n=== Edit Book Data ===\n")

        book_id = int(input("Enter the Book ID to edit stock: "))
        
        if book_id not in book:
            print("Book ID does not exist.")
            choice = input("Do you want to try again? (yes/no): ").strip().lower()
            if choice == "no":
                main_menu() 
                return 
            continue 
            
        new_stock = int(input(f"Enter new stock for '{book[book_id]['book_name']}': "))
        book[book_id]['stock'] = new_stock
        print(f"Stock for '{book[book_id]['book_name']}' has been updated to {new_stock}.")
    
        input("\nEnter to return to Main Menu.")
        main_menu()

def delete_book(): # Menu 6: Delete Book (DELETE)
    while True:
        print("\n=== Delete Book Data ===\n")

        book_id = int(input("Enter the Book ID to delete: "))
        
        if book_id not in book:
            print("Book ID does not exist.")
            choice = input("Do you want to try again? (yes/no): ").strip().lower()
            if choice == "no":
                main_menu() 
                return
            continue 
            
        deleted_book = book.pop(book_id)
        print(f"Book '{deleted_book['book_name']}' has been deleted.")
    
        input("\nEnter to return to Main Menu.")
        main_menu()

def exit_menu(): # Menu 7: Exit Menu
    print("Thank you for visiting BorrowBook^^ See you next time :) \n")
    input("\nEnter to return to Login.")
    login()
    

login()

