import time
from selenium import webdriver
import calender as calenderFile



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
    driver.get('https://www.expedia.com')
    time.sleep(1)  # Let the user actually see something!
    # Move the user to the flights page.
    flight_bt = driver.find_element_by_xpath("//a[@href='?pwaLob=wizard-flight-pwa']")
    flight_bt.click()
    # Taking a short break
    time.sleep(1)

    GoingToField_1 = driver.find_element_by_xpath("//div[@class='uitk-typeahead']")
    GoingToField_1.click()
    time.sleep(0.5)
    GoingToField_2 = driver.find_element_by_xpath("//div/input[@placeholder='Where are you leaving from?']")
    GoingToField_2.send_keys("Paris")
    time.sleep(1)
    GoingToField_3 = driver.find_element_by_xpath("//div/ul[@class='uitk-typeahead-results no-bullet']/li[1]")
    GoingToField_3.click()
    time.sleep(0.5)

    destinationField_1 = driver.find_element_by_xpath("//div[@class='uitk-typeahead' and @data-stid='location-field-leg1-destination']")
    destinationField_1.click()
    time.sleep(1)
    destinationField_2 = driver.find_element_by_xpath("//div/input[@placeholder='Where are you going to?']")
    destinationField_2.send_keys("Djibouti")
    time.sleep(1)
    destinationField_3 = driver.find_element_by_xpath("//div/ul[@class='uitk-typeahead-results no-bullet' and @data-stid='location-field-leg1-destination-results']/li[1]")
    destinationField_3.click()
    time.sleep(2)

    dateDeparture = driver.find_element_by_id("d1-btn")
    dateDeparture.click()

    manager_dp = calenderFile.Manager(5)
    manager_arr = calenderFile.Manager(7)
    row_dp, column_dp = manager_dp.retrieve_row_and_column(10)
    row_arr, column_arr = manager_arr.retrieve_row_and_column(8)
    departure_date_field = driver.find_element_by_xpath("//div/div[2]/table[@class='uitk-date-picker-weeks']/tbody/tr[{}]/td[{}]".format(row_dp + 1, column_dp + 1))
    departure_date_field.click()
    done_button = driver.find_element_by_xpath("//div/button[@data-stid='apply-date-picker']")
    done_button.click()
    time.sleep(5)

    arrival_field = driver.find_element_by_id("d2-btn")
    arrival_field.click()
    time.sleep(2)
    next_btn = driver.find_element_by_xpath("//div[@class='uitk-calendar']/div/button[2]")
    next_btn.click()

    #next_btn.click()
    time.sleep(3)
    return_date_field = driver.find_element_by_xpath("//div/div[2]/table[@class='uitk-date-picker-weeks']/tbody/tr[{}]/td[{}]/button".format(row_arr + 1, column_arr + 1))
    return_date_field.click()
    done_button = driver.find_element_by_xpath("//div/button[@data-stid='apply-date-picker']")
    done_button.click()
    time.sleep(5)
    driver.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
