import string

def generate_files():
    for letter in string.ascii_uppercase:
        with open(letter + ".txt", 'w') as file:
            pass  # пустой файл

generate_files()
