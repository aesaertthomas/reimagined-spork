#Thomas Aesaert
morse_dictionary = {}


def read_morse_file(path : str):
    
    with open(path, "r") as file:
        next(file) #This skips one line in the file

        for line in file:
            line.strip() #This line removes all the new line characters and removes trailing whitespace
            parts = line.split(";")
            parts[1] = parts[1].replace("\n","")
            morse_dictionary.update({parts[0] : parts[1]})


def translate_letter(letter : str) -> str:
    return morse_dictionary[letter]

def translate_text_in_morse(word : str) -> str:
    translation = ""
    for letter in word.lower():
        translation += f"{translate_letter(letter=letter)}  "
    return translation

read_morse_file("doc/Morse.txt")

letter = input("Enter a letter: ")
print(f"The translation of {letter} is: {translate_letter(letter=letter)}")

word = input("Enter a word: ")
print(f"The translation of {word} is {translate_text_in_morse(word)}")
