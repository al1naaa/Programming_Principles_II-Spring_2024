def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file)

filename = "your_text_file.txt"
print("Number of lines:", count_lines(filename))
