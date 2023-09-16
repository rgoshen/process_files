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


def prepend_date_to_files(directory, date):
    """Prepends the provided date to all files in the directory.

    Args:
        directory (str): The path to the directory.
        date (str): The date string to prepend.
    """
    # Get the list of visible files in the directory.
    visible_files = get_visible_files(directory)

    # Prepend the date to each file name
    for index, file in enumerate(visible_files):
        # Join the directory path with the new file name
        new_file_path = os.path.join(directory, f"{date}_{file}")
        # Rename the file with the new name
        os.rename(os.path.join(directory, file), new_file_path)
        # Update the list of visible files with the new name
        visible_files[index] = new_file_path

    print_directory_files(directory)


def print_directory_files(directory):
    """Processes the given directory.

    Args:
        directory (str): The path to the directory.
    """

    # Get the list of visible files in the current directory.
    visible_files = get_visible_files(directory)

    # Print out the names of all the visible files (including prepended date)
    for file in visible_files:
        print(file)
