import os
import unittest
from datetime import datetime
from io import StringIO
from unittest.mock import patch

from process_files_module import (
    get_visible_files,
    prepend_date_to_files,
    print_directory_files,
)


# Create a temporary directory for testing.
class TestProcessFiles(unittest.TestCase):
    def setUp(self):
        self.test_directory = "test_dir"
        os.mkdir(self.test_directory)
        with open(os.path.join(self.test_directory, "file1.txt"), "w") as f:
            f.write("Content 1")
            with open(os.path.join(self.test_directory, "file2.txt"), "w") as f:
                f.write("Content 2")
        with open(os.path.join(self.test_directory, ".hidden_file.txt"), "w") as f:
            f.write("Content 3")

    def tearDown(self):
        # Remove the files first
        for filename in os.listdir(self.test_directory):
            file_path = os.path.join(self.test_directory, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        # Then remove the directory
        os.rmdir(self.test_directory)

    def test_get_visible_files(self):
        # Test the get_visible_files function.
        visible_files = get_visible_files(self.test_directory)
        self.assertIn("file1.txt", visible_files)
        self.assertIn("file2.txt", visible_files)
        self.assertNotIn(".hidden_file.txt", visible_files)

    def test_print_directory_files(self):
        # Test the read_directory function.
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            print_directory_files(self.test_directory)
            output = mock_stdout.getvalue()

        self.assertIn("file1.txt", output)
        self.assertIn("file2.txt", output)
        self.assertNotIn(".hidden_file.txt", output)

    def test_prepend_date_to_files_with_current_date(self):
        # Test the prepend_date_to_files function.

        # Get the current date
        current_date = datetime.now().strftime("%Y-%m-%d")

        # Stub the get_visible_files function
        with patch("process_files_module.get_visible_files") as mock_get_visible_files:
            # Mock the return value of get_visible_files
            mock_get_visible_files.return_value = ["file1.txt", "file2.txt"]

        # Call the function to prepend the date
        prepend_date_to_files(self.test_directory, current_date)

        # Check if the file has been renamed with the date prefix
        renamed_files = os.listdir(self.test_directory)
        for filename in renamed_files:
            if filename != ".hidden_file.txt":
                self.assertTrue(filename.startswith(f"{current_date}_"))
            else:
                self.assertFalse(filename.startswith(f"{current_date}_"))

    def test_prepend_date_to_files_with_custom_date(self):
        # Test the prepend_date_to_files function.

        custom_date = "2020-01-01"

        # Call the function to prepend the date
        prepend_date_to_files(self.test_directory, custom_date)

        # Check if the file has been renamed with the date prefix
        renamed_files = os.listdir(self.test_directory)
        for filename in renamed_files:
            if filename != ".hidden_file.txt":
                self.assertTrue(filename.startswith(f"{custom_date}_"))
            else:
                self.assertFalse(filename.startswith(f"{custom_date}_"))

    def test_prepend_time_to_files_with_current_time(self):
        # Test the prepend_time_to_files function.

        # Get the current time
        current_time = datetime.now().strftime("%H:%M:%S")

        # Stub the get_visible_files function
        with patch("process_files_module.get_visible_files") as mock_get_visible_files:
            # Mock the return value of get_visible_files
            mock_get_visible_files.return_value = ["file1.txt", "file2.txt"]

        # Call the function to prepend the date
        prepend_date_to_files(self.test_directory, current_time)

        # Check if the file has been renamed with the date prefix
        renamed_files = os.listdir(self.test_directory)
        for filename in renamed_files:
            if filename != ".hidden_file.txt":
                self.assertTrue(filename.startswith(f"{current_time}_"))
            else:
                self.assertFalse(filename.startswith(f"{current_time}_"))

    def test_prepend_time_to_files_with_custom_time(self):
        # Test the prepend_date_to_files function.

        custom_time = "09:30:45"

        # Call the function to prepend the date
        prepend_date_to_files(self.test_directory, custom_time)

        # Check if the file has been renamed with the date prefix
        renamed_files = os.listdir(self.test_directory)
        for filename in renamed_files:
            if filename != ".hidden_file.txt":
                self.assertTrue(filename.startswith(f"{custom_time}_"))
            else:
                self.assertFalse(filename.startswith(f"{custom_time}_"))


if __name__ == "__main__":
    unittest.main()
