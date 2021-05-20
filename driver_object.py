import datetime
import time
from selenium import webdriver
import classes as objects


class ExpediaScraper:

    def __init__(self, user):
        self.user = user
        # Optional argument, if not specified will search path.
        self.driver = webdriver.Chrome()

    def start_selenium(self):

        self.driver.get('https://www.expedia.com')
        time.sleep(1)  # Let the user actually see something!
        self.flights_dep()
        self.user_departing_from(self.user.from_where)
        self.user_going_to(self.user.to_where)
        self.find_fill_dp_field()
        self.find_fill_arr_field()
        self.find_click_search_bt()
        airline_info, price = self.find_lowest_price()
        print(airline_info, price)
        self.driver.quit()

    def flights_dep(self):
        # Move the user to the flights page.
        flight_bt = self.driver.find_element_by_xpath("//a[@href='?pwaLob=wizard-flight-pwa']")
        flight_bt.click()
        # Taking a short break
        time.sleep(1)

    def user_departing_from(self, place):

        going_to_field_1 = self.driver.find_element_by_xpath("//div[@class='uitk-typeahead']")
        going_to_field_1.click()
        time.sleep(0.5)
        going_to_field_2 = self.driver.find_element_by_xpath("//div/input[@placeholder='Where are you leaving from?']")
        going_to_field_2.send_keys("{}".format(place))
        # Waits and give the website time to load a list.
        time.sleep(8)
        going_to_field_3 = self.driver.find_element_by_xpath("//div/ul[@class='uitk-typeahead-results no-bullet']/li[1]")
        going_to_field_3.click()
        time.sleep(1)

    def user_going_to(self, place):

        destination_field_xp = "//div[@class='uitk-typeahead' and @data-stid='location-field-leg1-destination']"
        destinationField_1 = self.driver.find_element_by_xpath(destination_field_xp)
        destinationField_1.click()
        time.sleep(1)
        destination_field_2 = self.driver.find_element_by_xpath("//div/input[@placeholder='Where are you going to?']")
        destination_field_2.send_keys("{}".format(place))
        # Waits and give the website time to load a list.
        time.sleep(8)
        destination_field_3_xp = "//div/ul[@class='uitk-typeahead-results no-bullet' and @data-stid='location-field-leg1-destination-results']/li[1]"
        destination_field_3 = self.driver.find_element_by_xpath(destination_field_3_xp)
        destination_field_3.click()
        time.sleep(1)

    def find_fill_dp_field(self):

        date_departure = self.driver.find_element_by_id("d1-btn")
        # Finds and retrieve the current month in the websites calendar.
        aria_label = date_departure.get_attribute("aria-label")
        current_date = datetime.datetime.strptime(aria_label[10:], "%B %w, %Y")

        nbr_of_click_dp = abs(current_date.month - (self.user.dp_date.month + 1))
        date_departure.click()

        manager_dp = objects.Manager(self.user.dp_date.month)
        row_dp, column_dp = manager_dp.retrieve_row_and_column(self.user.dp_date.day)
        next_btn_dp = self.driver.find_element_by_xpath("//div[@class='uitk-calendar']/div/button[2]")

        if nbr_of_click_dp > 0:
            for j in range(1, nbr_of_click_dp):
                next_btn_dp.click()
                time.sleep(2)
            departure_date_field_xp = "//div/div[2]/table[@class='uitk-date-picker-weeks']/tbody/tr[{}]/td[{}]"
        else:
            departure_date_field_xp = "//div/div[1]/table[@class='uitk-date-picker-weeks']/tbody/tr[{}]/td[{}]"

        departure_date_field = self.driver.find_element_by_xpath(
            departure_date_field_xp.format(row_dp + 1, column_dp + 1))
        departure_date_field.click()
        done_button = self.driver.find_element_by_xpath("//div/button[@data-stid='apply-date-picker']")
        done_button.click()
        time.sleep(3)

    def find_fill_arr_field(self):

        arrival_field = self.driver.find_element_by_id("d2-btn")
        arrival_field.click()
        arrival_date = self.user.arr_date
        manager_arr = objects.Manager(arrival_date.month)
        row_arr, column_arr = manager_arr.retrieve_row_and_column(arrival_date.day)
        next_btn_arr = self.driver.find_element_by_xpath("//div[@class='uitk-calendar']/div/button[2]")

        for i in range(1, self.user.nbr_of_click_arr):
            next_btn_arr.click()
            time.sleep(2)

        time.sleep(3)
        arr_date_field_xp = "//div/div[2]/table[@class='uitk-date-picker-weeks']/tbody/tr[{}]/td[{}]/button"
        return_date_field = self.driver.find_element_by_xpath(arr_date_field_xp.format(row_arr + 1, column_arr + 1))
        return_date_field.click()
        done_button = self.driver.find_element_by_xpath("//div/button[@data-stid='apply-date-picker']")
        done_button.click()
        time.sleep(3)

    def find_click_search_bt(self):

        bt_xpath = "//div/button[@data-testid='submit-button']"
        search_bt = self.driver.find_element_by_xpath(bt_xpath)
        search_bt.click()
        time.sleep(30)

    def find_lowest_price(self):

        price_xp = "//section//ul[@data-test-id='listings']/li[1]//span[@class='uitk-price-a11y is-visually-hidden']"
        airline_info_xp = "//section//ul[@data-test-id='listings']/li[1]//div[@data-test-id='flight-operated']"
        airline_info = self.driver.find_element_by_xpath(airline_info_xp)
        price_ticket = self.driver.find_element_by_xpath(price_xp)
        return airline_info.text, price_ticket.text
