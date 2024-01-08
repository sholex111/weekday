## scenario 1

from datetime import datetime


def get_weekday():
  date_str = input("Enter the date: ")
  try:
    date = datetime.strptime(date_str, "%d%m%Y")
  except ValueError:
    raise ValueError(
        "Invalid format. Please enter a date in the format 'ddmmyyyy'")

  # Get the day of the week as a string
  weekday = date.strftime("%A")
  print(f"The day {date_str} falls on a {weekday}.")


get_weekday()

