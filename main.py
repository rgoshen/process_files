import os

from process_files_module import read_directory

if __name__ == "__main__":
    # Get the list of visible files in the current directory.
    read_directory(os.getcwd())
