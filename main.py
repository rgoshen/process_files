import argparse
import os
from datetime import datetime

from date_validator import validate_date  # Import the function from date_validator.py
from time_validator import validate_time  # Import the function from time_validator.py
from process_files_module import (
    prepend_date_to_files,
    prepend_datetime_to_files,
    prepend_time_to_files,
)


def main():
    parser = argparse.ArgumentParser(
        description="Process a directory of visible files."
    )

    # Add the '-d' or '--directory' flag for the directory path
    parser.add_argument("-d", "--directory", help="Path to the directory to process")

    # Add the '-D' or '--date' flag for the date to append to the filename
    parser.add_argument(
        "-D",
        "--date",
        type=validate_date,
        nargs="?",
        const=datetime.now().strftime("%Y-%m-%d"),
        help="Date in 'YYYY-MM-DD' format",
    )

    # Add the '-t' or '--time' flag for the time to append to the filename
    parser.add_argument(
        "-t",
        "--time",
        type=validate_time,
        nargs="?",
        const=datetime.now().strftime("%H:%M:%S"),
        help="Time in 'HH:MM:SS' format",
    )

    args = parser.parse_args()

    # Determine the directory to process
    directory_to_process = args.directory if args.directory else os.getcwd()

    # Check if the specified directory exists
    if not os.path.exists(directory_to_process):
        print(f"Error: Directory '{directory_to_process}' does not exist.")
        return  # Exit early if the directory doesn't exist

    # Check which arguments are provided and calls the correct method
    if args.date and args.time:
        prepend_datetime_to_files(directory_to_process, args.date, args.time)
    elif args.date:
        prepend_date_to_files(directory_to_process, args.date)
    elif args.time:
        prepend_time_to_files(directory_to_process, args.time)

    print(f"Files in '{directory_to_process}' finished processing.")


if __name__ == "__main__":
    main()
