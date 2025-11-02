
from datetime import datetime
def days_between_dates(date1: str, date2: str, date_format: str = "%Y-%m-%d") -> int:
    """Return the number of days between two dates given in string format."""
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    return abs((d2 - d1).days)
   
# call the function and print the result

if __name__ == "__main__":
    print(days_between_dates("2023-01-01", "2023-01-31"))  # 30
    print(days_between_dates("2022-05-15", "2022-06-15"))  # 31
    print(days_between_dates("2020-02-01", "2020-03-01"))  # 29
    print(days_between_dates("2019-12-25", "2020-01-01"))  # 7
    print(days_between_dates("2021-07-04", "2021-07-14"))  # 10
    print(days_between_dates("2022-11-11", "2022-12-11"))  # 30