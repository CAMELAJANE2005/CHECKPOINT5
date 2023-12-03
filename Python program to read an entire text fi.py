 Python program to read an entire text file:
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("File not found.")


file_name = "example.txt"  # Replace with the name of your text file
file_content = read_file(file_name)
print(file_content)


Python program to read the first n lines of a file:


def read_first_n_lines(file_name, n):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines[:n]:
                print(line.rstrip())
    except FileNotFoundError:
        print("File not found.")


file_name = "example.txt"  # Replace with the name of your text file
n = 5  # Number of lines to read
read_first_n_lines(file_name, n)


Python program to read the last n lines of a file:
def read_last_n_lines(file_name, n):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines[-n:]:
                print(line.rstrip())
    except FileNotFoundError:
        print("File not found.")


file_name = "example.txt"  # Replace with the name of your text file
n = 5  # Number of lines to read
read_last_n_lines(file_name, n)


Python program to count the number of words in a text file:
def count_words(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print("File not found.")


file_name = "example.txt"  # Replace with the name of your text file
word_count = count_words(file_name)
print("Number of words:", word_count)


Python program to read the last n lines of a file (bonus):
def read_last_n_lines(file_name, n):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines[-n:]:
                print(line.rstrip())
    except FileNotFoundError:
        print("File not found.")


file_name = "example.txt"  # Replace with the name of your text file
n = 5  # Number of lines to read
read_last_n_lines(file_name, n)
