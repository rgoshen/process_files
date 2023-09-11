import os


def main():
    # Get the current working directory
    current_directory = os.getcwd()

    # List all the files in the current directory
    files = os.listdir(current_directory)

    # Create a list of all the visible files
    visible_files = []

    # Print out the names of all the files
    for file in files:
        # Check if the file is hidden
        if not file.startswith("."):
            # Add the file to the list of visible files
            visible_files.append(file)

    # Print out the names of all the visible files
    for file in visible_files:
        print(file)


if __name__ == "__main__":
    main()
