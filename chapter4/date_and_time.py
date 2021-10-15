"""
4.7 (Date and Time) Python’s datetime module contains a datetime type with a
method today that returns the current date and time as a datetime object. Write a parameterless date_and_time function containing the following statement, then call that function to display the current date and time:
print(datetime.datetime.today())
On our system, the date and time display in the following format:
2018-06-08 13:04:19.214180
"""
from datetime import datetime


def date_time():
    return datetime.today()


print(date_time())
