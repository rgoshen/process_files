import unittest
import argparse

from time_validator import validate_time


class TestTimeValidator(unittest.TestCase):
    def test_valid_time(self):
        # Test a valid time string
        valid_time_str = "12:34:56"
        result = validate_time(valid_time_str)
        self.assertEqual(result, valid_time_str)

    def test_invalid_format(self):
        # Test an invalid time string format
        invalid_format_str = "1234:56"
        with self.assertRaises(argparse.ArgumentTypeError):
            validate_time(invalid_format_str)

    def test_invalid_time(self):
        # Test an invalid time string (e.g., 25 hours)
        invalid_time_str = "25:00:00"
        with self.assertRaises(argparse.ArgumentTypeError):
            validate_time(invalid_time_str)


if __name__ == "__main__":
    unittest.main()
