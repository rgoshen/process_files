import argparse
import os

from process_files_module import read_directory


def main():
    parser = argparse.ArgumentParser(
        description="Process a directory of visible files."
        )

    # Add the '-d' or '--directory' flag for the directory path
    parser.add_argument(
        "-d", "--directory", help="Path to the directory to process"
        )

    args = parser.parse_args()

    # Determine the directory to process
    directory_to_process = args.directory if args.directory else os.getcwd()

    # Check if the specified directory exists
    if not os.path.exists(directory_to_process):
        print(f"Error: Directory '{directory_to_process}' does not exist.")
        return  # Exit early if the directory doesn't exist

    # Call read_directory with the specified or default directory
    read_directory(directory_to_process)


if __name__ == "__main__":
    main()
