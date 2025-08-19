# Function to open and read a file
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count():
    text = get_book_text("./books/frankenstein.txt")
    return len(text.split())

def main():
    num_words = word_count()
    print(f"{num_words} words found in the document")

main()