import os
import unittest
from io import StringIO
from unittest.mock import patch

from process_files_module import (
    get_visible_files,
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


if __name__ == "__main__":
    unittest.main()
