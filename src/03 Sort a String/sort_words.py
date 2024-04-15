def sort_words(words):
    words_split=words.split()
    res=sorted(words_split,key=str.casefold)
    
    return ' '.join(res)

# commands used in solution video for reference
if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))  # apple banana ORANGE
