from datetime import datetime

def to_date(date_string):
    # Convert the date string to a datetime object
    date_object = datetime.strptime(date_string, "%Y-%m-%d")
    return date_object