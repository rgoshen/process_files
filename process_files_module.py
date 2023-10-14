import os
import subprocess
from datetime import datetime

import colorama

from proress_bar import progress_bar
from utilities import get_visible_files, print_directory_files


def prepend_date_time_to_files(directory, date=None, time=None):
    """Prepends the provided date and/or time to all files in the directory.

    Args:
        directory (str): The path to the directory.
        date (str, optional): The date string to prepend. Defaults to current date if not provided.
        time (str, optional): The time string to prepend. Defaults to current time if not provided.
    """

    # Use provided date or default to current date
    date_to_use = date if date else datetime.now().strftime("%Y-%m-%d")
    formatted_date = date_to_use.replace("-", "")

    # Use provided time or default to current time
    time_to_use = time if time else datetime.now().strftime("%H:%M:%S")
    formatted_time = time_to_use.replace(":", "")

    # Get the list of visible files in the directory.
    visible_files = get_visible_files(directory)

    file_count = 0
    total_files = len(visible_files)

    # Prepend the formatted date and time to each file name
    for index, file in enumerate(visible_files):
        # Join the directory path with the new file name
        new_file_path = os.path.join(directory, f"{formatted_date}_{formatted_time}_{file}")
        # Rename the file with the new name
        os.rename(os.path.join(directory, file), new_file_path)
        # Update the list of visible files with the new name
        visible_files[index] = new_file_path
        file_count += 1
        progress_bar(file_count, total_files)

    print(colorama.Fore.RESET)
    print_directory_files(directory)


def change_file_creation_date(directory, new_date=None, new_time=None):
    if new_date is None and new_time is None:
        # If both new_date and new_time are not provided, set both to the current date and time
        new_datetime = datetime.now()
    else:
        # If only one of new_date or new_time is provided, set the other to the current date or time
        new_date = datetime.strptime(new_date, '%Y-%m-%d').date() or datetime.now().date()
        new_time = datetime.strptime(new_time, '%H:%M:%S').time() or datetime.now().time()
        new_datetime = datetime.combine(new_date, new_time)

        # Format the new datetime as YYYYMMDDHHMM.SS
    formatted_datetime = new_datetime.strftime("%Y%m%d%H%M.%S")

    # Get the list of visible files in the directory.
    visible_files = get_visible_files(directory)

    # Iterate through the files in the directory and change their creation date
    for index, file in enumerate(visible_files):
        file_path = os.path.join(directory, file)
        subprocess.run(["touch", "-t", formatted_datetime, file_path])
