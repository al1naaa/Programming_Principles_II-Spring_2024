def write_list_to_file(filename, lst):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(str(item) + '\n')

filename = "your_output_file.txt"
my_list = ["item1", "item2", "item3"]
write_list_to_file(filename, my_list)
