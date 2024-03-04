import time

import safsarX_selling_Tickets.data_of_elements.data
from safsarX_selling_Tickets.selling_tickets_page.driver import webdriver_instance, Actions

base_url = "https://portal-dev.safsarglobal.link/"
my_driver = webdriver_instance()


def navigation_to_selling_tickets(my_driver):
    my_driver.get(base_url)
    actions = Actions(my_driver)
    selling_tickets_button = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.selling_tickets_button)
    time.sleep(5)
    actions.click_element(selling_tickets_button)


navigation_to_selling_tickets(my_driver)
time.sleep(5)