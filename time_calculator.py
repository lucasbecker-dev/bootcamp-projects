# this where I would import datetime to make this all much simpler in real life

def add_time(start, duration, start_day=None):

  # for calculating start_day and new day of the week more easily
  days_of_the_week_reference = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
  ]

  # pull out needed strings from parameters
  start_elements = start.split()
  start_AMPM = start_elements[1]
  start_time = start_elements[0].split(":")
  duration_time = duration.split(":")
  day_of_the_week = ""

  # convert start_time to 24 hour format
  if start_AMPM == "PM":
    start_time[0] = str(int(start_time[0]) + 12)
  
  # determine how many days have been added and generate note if needed
  
  #days_added = int((int(duration_time[0]) / 24) + (int(duration_time[1]) / 1440))
  #if (int(duration_time[0]) + int(start_time[0])) > 24:
  #  days_added += 1
  


  # calculate new hours and minutes
  new_hour = int(int(start_time[0]) + int(duration_time[0]))
  new_minute = int(int(start_time[1]) + int(duration_time[1]))
  days_added = 0
  while new_minute >= 60:
    new_hour += 1
    new_minute -= 60
  while new_hour >= 24:
    days_added += 1
    new_hour -= 24
  if new_minute < 10:
    new_minute = F"0{new_minute}"

  # convert answer back to 12 hour format
  new_AMPM = "AM"
  if new_hour >= 12:
    new_hour -= 12
    new_AMPM = "PM"
  if new_hour == 0:
    new_hour = 12

  # if start_day was specified in the args, calculate new one
  days_later_str = ""
  if start_day != None:
    day_of_the_week = days_of_the_week_reference[int((days_of_the_week_reference.index(start_day.capitalize()) + days_added) % 7)]
    days_later_str += F", {day_of_the_week}"
  if days_added == 1:
    days_later_str += " (next day)"
  elif days_added >= 2:
    days_later_str += F" ({days_added} days later)"

  # put together pieces and return new_time
  new_time = F"{new_hour}:{new_minute} {new_AMPM}{days_later_str}"
  return new_time