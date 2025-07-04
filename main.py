from stats import word_count
from stats import char_count
from stats import sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
    
def main():
    if len(sys.argv) != 2: 
        # Path to book

        print(f"Usage: python3 main.py <path_to_book>")
        
        sys.exit(1)
            
    path = sys.argv[1]
    
    # Header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    
    book_str = get_book_text(path)
    
    count = word_count(book_str)
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    
    alpha_count = char_count(book_str.lower())
    
    sorted = sorted_list(alpha_count)
    
    for i in sorted: 
        print(f"{i['char']}: {i['num']}")
    
    # Footer
    print("============= END ===============")

main()