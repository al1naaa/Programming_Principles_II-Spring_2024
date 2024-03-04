import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("File deleted successfully.")
        else:
            print("No write access to the file.")
    else:
        print("File does not exist.")

path = "your_specified_file_path_here"
delete_file(path)
