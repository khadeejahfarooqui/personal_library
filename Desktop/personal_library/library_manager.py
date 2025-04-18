# 📖 Reader’s Paradise - Your Personal Library Manager


my_shelf = []

def show_menu():
    print("\n📌 What would you like to do?")
    print("1️⃣  📥 Add Book to Shelf")
    print("2️⃣  📚 Show All Books")
    print("3️⃣  🗑️ Remove a Book")
    print("4️⃣  🔍 Search for a Book")
    print("5️⃣  📊 View Statistics")
    print("6️⃣  ❌ Exit Library")


def add_book():
    print("\n✨ Let's Add a New Book ✨")
    title = input("📖 Book Title: ")
    author = input("✍️  Author Name: ")
    year = int(input("📅 Year of Publication: "))
    genre = input("🎭 Genre: ")
    read_input = input("👓 Have you read it? (yes/no): ").lower()
    read = True if read_input == "yes" else False

    book = {
        "Title": title,
        "Author": author,
        "Year": year,
        "Genre": genre,
        "Read": read
    }

    my_shelf.append(book)
    print("✅ Book added to your shelf!")

def show_books():
    print("\n📚 Your Book Shelf:")
    if not my_shelf:
        print("😕 No books added yet.")
    else:
        for index, book in enumerate(my_shelf, start=1):
            status = "✔️ Read" if book["Read"] else "❌ Not Read"
            print(f"{index}. \"{book['Title']}\" by {book['Author']} ({book['Year']}) - {book['Genre']} - {status}")
            print("--------------------------------------------------")

# 🗑️ Yeh remove_book function alag hona chahiye, show_books ke andar nahi
def remove_book():
    print("\n❌ Remove a Book from Shelf")
    if not my_shelf:
        print("📭 Your shelf is empty. Nothing to remove.")
        return

    title_to_remove = input("🗑️ Enter the book title to remove: ").strip().lower()

    found = False
    for book in my_shelf:
        if book["Title"].lower() == title_to_remove:
            my_shelf.remove(book)
            found = True
            print(f"✅ \"{book['Title']}\" removed from your shelf.")
            break

    if not found:
        print("⚠️ Book not found. Please check the title and try again.")
def search_books():
    print("\n🔍 Search Your Shelf")
    if not my_shelf:
        print("📭 Your shelf is empty. Nothing to search.")
        return

    print("1️⃣ Search by Title")
    print("2️⃣ Search by Author")
    search_choice = input("👉 Enter your choice (1 or 2): ")

    if search_choice == "1":
        keyword = input("🔠 Enter title to search: ").strip().lower()
        results = [book for book in my_shelf if keyword in book["Title"].lower()]
    elif search_choice == "2":
        keyword = input("✍️ Enter author to search: ").strip().lower()
        results = [book for book in my_shelf if keyword in book["Author"].lower()]
    else:
        print("⚠️ Invalid choice. Please select 1 or 2.")
        return

    if results:
        print("\n✅ Matching Books Found:")
        for index, book in enumerate(results, start=1):
            status = "✔️ Read" if book["Read"] else "❌ Not Read"
            print(f"{index}. \"{book['Title']}\" by {book['Author']} ({book['Year']}) - {book['Genre']} - {status}")
            print("--------------------------------------------------")
        else:
           print("😕 No matching books found.")

def show_stats():
    print("\n📊 Library Stats")
    total = len(my_shelf)

    if total == 0:
        print("📭 Your shelf is empty. No stats to show.")
        return

    read_books = sum(1 for book in my_shelf if book["Read"])
    percentage = (read_books / total) * 100

    print(f"📚 Total books: {total}")
    print(f"✔️ Books read: {read_books}")
    print(f"📈 Read percentage: {percentage:.1f}%")




# 🚪 Main Program Loop
while True:
    show_menu()
    choice = input("👉 Enter your choice (1/2/3/4/5/6): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        show_books()
    elif choice == "3":
        remove_book()
    elif choice == "4":
        search_books()
    elif choice == "5":
        show_stats()
    elif choice == "6":
        print("👋 Exiting Reader’s Paradise. Have a great day!")
        break
    else:
        print("⚠️ Invalid option. Try again.")
