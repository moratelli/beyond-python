# big O doesn't matter when n is small, and n is usually small

# to determine the big O notation for a piece of code, we must do 4 tasks:
# - identify what the n is (size of the input date the code works on)
# - count the steps in the code
# - drop the lower orders
# - drop the coefficients

def reading_list(books):
    print('Here are the book I will read:')   # 1 step
    number_of_books = 0                       # 1 step
    for book in books:                        # n * 2 (steps in the loop)
        print(book)                           # (already counted)
        number_of_books += 1                  # (already counted)
    print(number_of_books, 'books total.')    # 1 step

# 2n + 3 -- or (1 + 1 + (n * 2) + 1)
# big O doesn't intend to describe specifics, so we drop the lower orders
# 2n
# next, we drop the coefficients. in this case, it's 2
# n
# final big O = O(n) -- linear time complexity
# if the books list increases tenfold in size, the runtime increases tenfold as well


def find_duplicate_books(books):
    for i in range(books):                       # n steps
        for j in range(i + 1, books):            # n steps
            if books[i] == books[j]:             # 1 step
                print('Duplicate:', books[i])    # 1 step

# final big O = O(n(pow2)) -- polynomial time operation
# nested loops alone don't imply a polynomial time operation but nested loops where
#   both loops iterate n times do. these result in n(pow2) steps
