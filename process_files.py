import os


def main():
    # Get the current working directory
    current_directory = os.getcwd()

    # List all the files in the current directory
    files = os.listdir(current_directory)

    # Print out the names of all the files
    for file in files:
        print(file)


if __name__ == "__main__":
    main()
