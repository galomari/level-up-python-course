import random
from docx import Document

def generate_prephrase(number_of_words):
    # Load the DOCX file
    doc = Document(r"C:\Users\hp\Downloads\f.docx")
    # Read all text from the first paragraph
    line = doc.paragraphs[0].text
    words = line.split()
    # Filter words that match the specified length
    words_of_length = [word for word in words if len(word) == number_of_words]
    # Randomly choose a word from the filtered list
    if words_of_length:
        return random.choice(words_of_length)
    return None

# Example usage
print(generate_prephrase(9))
