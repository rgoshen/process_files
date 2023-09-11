import os


def get_visible_files(directory):
    """Gets a list of all the visible files in the given directory.

    Args:
        directory (str): The path to the directory.

    Returns:
        list: A list of all the visible files in the directory.
    """

    # Get the list of files in the directory.
    files = os.listdir(directory)

    # Create a list of all the visible files.
    visible_files = []

    # Iterate through the list of files.
    for file in files:
        # Check if the file is hidden.
        if not file.startswith("."):
            # Add the file to the list of visible files.
            visible_files.append(file)

    return visible_files


def read_directory(directory):
    """Processes the given directory.

    Args:
        directory (str): The path to teh directory.
    """

    # Get the list of visible files in the current directory.
    visible_files = get_visible_files(directory)

    # Print out the names of all the visible files.
    for file in visible_files:
        print(file)
