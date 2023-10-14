import os
import unittest
from datetime import datetime, timedelta
from unittest.mock import patch

from process_files_module import change_file_creation_date, prepend_date_time_to_files
from utilities import get_visible_files


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

    def test_change_file_creation_date_with_current_datetime(self):
        # Test changing the creation date with the current date and time
        current_datetime = datetime.now()
        change_file_creation_date(self.test_directory)
        visible_files = get_visible_files(self.test_directory)

        for filename in visible_files:
            file_path = os.path.join(self.test_directory, filename)
            file_stat = os.stat(file_path)
            file_creation_datetime = datetime.fromtimestamp(file_stat.st_ctime)
            # Ensure the file's creation date is close to the current date and time
            self.assertLessEqual(
                abs(current_datetime - file_creation_datetime), timedelta(seconds=1)
                )

    def test_change_file_creation_date_with_custom_datetime(self):
        # Test changing the creation date with a custom date and time
        custom_date = datetime(2020, 1, 1)
        custom_time = datetime(2020, 1, 1, 12, 0, 0)
        change_file_creation_date(self.test_directory, custom_date, custom_time)
        visible_files = get_visible_files(self.test_directory)

        for filename in visible_files:
            file_path = os.path.join(self.test_directory, filename)
            file_stat = os.stat(file_path)
            file_creation_datetime = datetime.fromtimestamp(file_stat.st_ctime)
            # Ensure the file's creation date is the custom date and time
            self.assertEqual(file_creation_datetime, datetime(2020, 1, 1, 12, 0, 0))

    def test_change_file_creation_date_with_hidden_files(self):
        # Test changing the creation date while ignoring hidden files
        custom_date = datetime(2020, 1, 1)
        custom_time = datetime(2020, 1, 1, 12, 0, 0)
        change_file_creation_date(self.test_directory, custom_date, custom_time)
        visible_files = get_visible_files(self.test_directory)

        for filename in visible_files:
            file_path = os.path.join(self.test_directory, filename)
            file_stat = os.stat(file_path)
            file_creation_datetime = datetime.fromtimestamp(file_stat.st_ctime)
            # Ensure the file's creation date is the custom date and time
            self.assertEqual(file_creation_datetime, datetime(2020, 1, 1, 12, 0, 0))


if __name__ == "__main__":
    unittest.main()
