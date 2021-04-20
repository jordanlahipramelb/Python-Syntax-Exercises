# help(str)


def print_upper_words(words):
    """Prints out each word on a separate line, but in all uppercase.
    
    words is list
    """
    
    for word in words:
        print(word.upper())
        
        
# print_upper_words(["Programming", "is", "pretty", "fun"])

def print_upper_words_with_e(words):
    """Prints out each word on a separate line that start with the letter ‘e’ , but in all uppercase.

    Args:
        words (list): list of words
    """
    
    for word in words:
        if word.startswith('E') or word.startswith('e'):
            print(word.upper())
            
# print_upper_words_with_e(["eagle", "Edward", "Alfred"])

def print_upper_words2(words, must_start_with):
    """Pass in a set of letters, and it only prints upper case words that start with one of those letters

    Args:
        words (list): list of words
        must_start_with (str): first letter of words you want uppercased
    """
    
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                

# print_upper_words2(["eagle", "Edward", "Alfred", "zope"], must_start_with=["A", "E"])