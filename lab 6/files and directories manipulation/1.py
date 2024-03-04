import os

def list_directories_and_files(path):
    directories = []
    files = []
    all_directories_and_files = []

    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            directories.append(item)
        else:
            files.append(item)
        all_directories_and_files.append(item)

    print("Directories:", directories)
    print("Files:", files)
    print("All Directories and Files:", all_directories_and_files)

path = "your_specified_path_here"
list_directories_and_files(path)