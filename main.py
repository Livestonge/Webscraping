import time
from selenium import webdriver




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
    driver.get('https://www.expedia.com');
    time.sleep(1)  # Let the user actually see something!
    flight_bt = driver.find_element_by_class_name("uitk-tab-anchor")
    flight_bt[2].click()
    driver.quit()
    #time.sleep(5)  # Let the user actually see something!


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
