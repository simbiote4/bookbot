def read_book(book):
    with open(book) as b:
        book_text = b.read()
    return book_text

def word_count(book):
    text = read_book(book)
    return len(text.split())

def letter_count(book):
    letter_dict = {}
    book_text = read_book(book)
    for i in book_text:
        if i.lower() in letter_dict:
            letter_dict[i.lower()] += 1
        else:
            letter_dict[i.lower()] = 1
    return letter_dict

def sort_on(letter): # Selects the sort value to be the dictionary with key <"num">
    return letter["num"]


# Returns book file path, word count, and sorted list of dictionaries
# containting Key = 'char' and Value = count of char appearance.
def book_report(book):
    print(f"""============ BOOKBOT ============
Analyzing book found at {book}
----------- Word Count ----------
Found {word_count(book)} total words
--------- Character Count -------""")
    book_letters = letter_count(book) # Store returned dictionary of letter count to a variable
    letters_sorted = [] # Create empty list to store the split and sorted dictionaries from <book_letters>
    for letter in book_letters: # Loop to iterate through the dictionary or book_letters
        if letter.isalpha(): # Check if dictionary key character is alpha
            letters_sorted.append({"char": letter, "num": book_letters[letter]}) # If alpha then add to the list <letters_sorted>
    letters_sorted.sort(reverse=True, key=sort_on) # Reverse sort the list on the value. Uses the fucntion <sort_on> to determine which value to use
    for i in letters_sorted: # Iterate through the now sorted list and print the values on a seprate line
        print(f"{i["char"]}: {i["num"]}")
    return
