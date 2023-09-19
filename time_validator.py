from datetime import datetime
import argparse


def validate_time(time_str):
    """
     Validate a time string in 'HH:MM:SS' format and ensure it represents a valid time.

    Args:
        time_str (str): The time string to validate.

    Returns:
        str: The validated time string if it's in the correct format and represents a valid time.

    Raises:
        argparse.ArgumentTypeError: If the time string is not in the correct format or not a valid time.
    """
    try:
        # Attempt to parse the time string as a valid time
        datetime.strptime(time_str, "%H:%M:%S")
    except ValueError:
        raise argparse.ArgumentTypeError(
            "Invalid time format or not a valid time. Use 'HH:MM:SS' format."
        )

    return time_str
