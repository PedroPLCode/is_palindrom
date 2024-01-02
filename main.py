words_to_test = ["kajaK", "Potop", "mleko", "Python", "Tralalala", "oKo"]

def is_palindrom(str):
    """
        Returns True if str is palindrom,
        Else returns False.
        One argument: str - string to test.
        Optional arguments: None
    """
    str_to_test = str.lower()
    return True if str_to_test == str_to_test [::-1] else False

def check_words(list):
    """
        Use for loop to iterate through list of strings,
        Run is_palindrom() function for each of single words in list,
        And print results.
        One argument: List of strings to test with is_palindrom() function.
        Optional arguments: None
    """
    for item in list:
        print(f"is_palindrom('{item}'): {is_palindrom(item)}")
        
check_words(words_to_test)