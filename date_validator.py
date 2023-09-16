import argparse
import datetime


def validate_date(date_str):
    """
        Validates a date string in 'YYYY-MM-DD' format.

        Args:
            date_str (str): The date string to validate.

        Returns:
            str: The valid date string if the input is in 'YYYY-MM-DD' format.

        Raises:
            argparse.ArgumentTypeError: If the input date string is not in
            the correct format.

        Example:
            >>> validate_date("2023-09-11")
            '2023-09-11'
        """
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return date_str
    except ValueError:
        raise argparse.ArgumentTypeError(
            "Invalid date format. Please use 'YYYY-MM-DD'."
            )
