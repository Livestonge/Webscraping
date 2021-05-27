import classes as calender_file
import driver_object as driver
import sys


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Ask the user for input
    departing_from = input("Where are you departing from: ")
    destination = input("Where are you going to?")
    month_dp = int(input("Which month are you leaving? f.ex 01 for January"))
    day_dp = int(input("Which day are you leaving?"))
    month_arr = int(input("Which month are you coming back? f.ex 02 for February"))
    day_arr = int(input("Which day are you coming back?"))

    # Since the program is using collections, we subtract 1 from the provided month number.
    dp_date = calender_file.Date(day_dp, month_dp - 1)
    arr_date = calender_file.Date(day_arr, month_arr - 1)

    user = calender_file.User(departing_from, destination, dp_date, arr_date)
    expedia_driver = driver.ExpediaScraper(user)
    expedia_driver.start_selenium()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
