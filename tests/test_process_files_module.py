import os
import unittest
from datetime import datetime
from unittest.mock import patch

from process_files_module import prepend_date_time_to_files


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

    def test_prepend_current_date_and_time_to_files(self):
        # Test the prepend_date_time_to_files function with using the current date and time.

        # Get the current date
        current_date = datetime.now().strftime("%Y-%m-%d")

        # Get the current time
        current_time = datetime.now().strftime("%H:%M:%S")

        # Combines the date and time to one string
        current_date_time = (
            f"{current_date.replace('-', '')}_{current_time.replace(':', '')}"
        )

        # Stub the get_visible_files function
        with patch("process_files_module.get_visible_files") as mock_get_visible_files:
            # Mock the return value of get_visible_files
            mock_get_visible_files.return_value = ["file1.txt", "file2.txt"]

        # Call the function to prepend the date
        prepend_date_time_to_files(self.test_directory, current_date, current_time)

        # Check if the file has been renamed with the date prefix
        renamed_files = os.listdir(self.test_directory)
        for filename in renamed_files:
            if filename != ".hidden_file.txt":
                self.assertTrue(filename.startswith(f"{current_date_time}_"))
            else:
                self.assertFalse(filename.startswith(f"{current_date_time}_"))

    def test_prepend_custom_date_and_time_to_files(self):
        # Test the prepend_date_time_to_files function with a custom date and time.

        # Get the current date
        custom_date = "2020-04-11"

        # Get the current time
        custom_time = "09:30:45"

        # Combines the date and time to one string
        custom_date_time = (
            f"{custom_date.replace('-', '')}_{custom_time.replace(':', '')}"
        )

        # Stub the get_visible_files function
        with patch("process_files_module.get_visible_files") as mock_get_visible_files:
            # Mock the return value of get_visible_files
            mock_get_visible_files.return_value = ["file1.txt", "file2.txt"]

        # Call the function to prepend the date
        prepend_date_time_to_files(self.test_directory, custom_date, custom_time)

        # Check if the file has been renamed with the date prefix
        renamed_files = os.listdir(self.test_directory)
        for filename in renamed_files:
            if filename != ".hidden_file.txt":
                self.assertTrue(filename.startswith(f"{custom_date_time}_"))
            else:
                self.assertFalse(filename.startswith(f"{custom_date_time}_"))

    def test_prepend_custom_date_to_files(self):
        # Test the prepend_date_time_to_files function with a custom date.

        # Get the current date
        custom_date = "2020-04-11"

        # Get the current time
        current_time = datetime.now().strftime("%H:%M:%S")

        # Combines the date and time to one string
        custom_date_time = (
            f"{custom_date.replace('-', '')}_{current_time.replace(':', '')}"
        )

        # Stub the get_visible_files function
        with patch("process_files_module.get_visible_files") as mock_get_visible_files:
            # Mock the return value of get_visible_files
            mock_get_visible_files.return_value = ["file1.txt", "file2.txt"]

        # Call the function to prepend the date
        prepend_date_time_to_files(self.test_directory, custom_date)

        # Check if the file has been renamed with the date prefix
        renamed_files = os.listdir(self.test_directory)
        for filename in renamed_files:
            if filename != ".hidden_file.txt":
                self.assertTrue(filename.startswith(f"{custom_date_time}_"))
            else:
                self.assertFalse(filename.startswith(f"{custom_date_time}_"))

    def test_prepend_custom_time_to_files(self):
        # Test the prepend_date_time_to_files function with a custom time.

        # Get the current date
        current_date = datetime.now().strftime("%Y-%m-%d")

        # Get the current time
        custom_time = "09:30:45"

        # Combines the date and time to one string
        custom_date_time = (
            f"{current_date.replace('-', '')}_{custom_time.replace(':', '')}"
        )

        # Stub the get_visible_files function
        with patch("process_files_module.get_visible_files") as mock_get_visible_files:
            # Mock the return value of get_visible_files
            mock_get_visible_files.return_value = ["file1.txt", "file2.txt"]

        # Call the function to prepend the date
        prepend_date_time_to_files(self.test_directory, time=custom_time)

        # Check if the file has been renamed with the date prefix
        renamed_files = os.listdir(self.test_directory)
        for filename in renamed_files:
            if filename != ".hidden_file.txt":
                self.assertTrue(filename.startswith(f"{custom_date_time}_"))
            else:
                self.assertFalse(filename.startswith(f"{custom_date_time}_"))


if __name__ == "__main__":
    unittest.main()
