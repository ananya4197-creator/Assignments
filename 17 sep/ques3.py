 # 3library management system

library = {
    "Harry Potter": 3,
    "Python Basics": 2,
    "Data Science": 1
}

#while True:
book = input("Enter book to borrow (or 'exit' to quit): ")
if book in library:
        if library[book] > 0:
            library[book] -= 1
            print(f"Issued '{book}'. Remaining: {library[book]}")
        else:
            print("Out of stock")
else:
    print("Not found")

# Write updated inventory to file
with open("library.txt", "w") as f:
    for title, quantity in library.items():
        f.write(f"{title} → {quantity}\n")

print("Updated inventory saved to library.txt")
