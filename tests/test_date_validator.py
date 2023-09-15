import argparse
import unittest

from date_validator import validate_date


class TestDateValidator(unittest.TestCase):

    def test_valid_date(self):
        # Test a valid date string
        valid_date_str = "2023-09-11"
        result = validate_date(valid_date_str)
        self.assertEqual(result, valid_date_str)

    def test_invalid_date(self):
        # Test an invalid date string
        invalid_date_str = "9-11-2023"  # Using '/' instead of '-'
        with self.assertRaises(argparse.ArgumentTypeError):
            validate_date(invalid_date_str)


if __name__ == "__main__":
    unittest.main()
