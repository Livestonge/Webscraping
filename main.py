import classes as calenderFile
import driver_object as driver



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    user = calenderFile.User("Paris", "Djibouti", calenderFile.Date(10, 5), calenderFile.Date(18, 8))
    expedia_driver = driver.Expedia_scraper(user)
    expedia_driver.start_selenium()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
