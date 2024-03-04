import os

def check_path(path):
    if os.path.exists(path):
        print("Filename:", os.path.basename(path))
        print("Directory Portion:", os.path.dirname(path))
    else:
        print("Path does not exist.")

path = "your_specified_path_here"
check_path(path)
