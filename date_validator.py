import argparse
import datetime


def validate_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return date_str
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid date format. Please use 'YYYY-MM-DD'.")
