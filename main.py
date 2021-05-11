import time
from selenium import webdriver




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
    time.sleep(2)
    driver.quit()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
