import re

def is_palindrome(phrase):
    phrase=phrase.lower()
    phrase=re.sub('[^A-Za-z]', '', phrase)
    return True if phrase == phrase[::-1] else False


# commands used in solution video for reference
if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
