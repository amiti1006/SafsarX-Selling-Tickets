import time
from selenium.webdriver.common.by import By

import safsarX_selling_Tickets.data_of_elements.data
from safsarX_selling_Tickets.selling_tickets_page.driver import webdriver_instance, Actions

base_url = "https://portal-dev.safsarglobal.link/"
my_driver = webdriver_instance()
my_driver.get(base_url)
actions = Actions(my_driver)


def navigation_to_selling_tickets():
    selling_tickets_button = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.selling_tickets_button)
    actions.click_element(selling_tickets_button)
    account_exist_button = actions.find_element(
        (By.XPATH, '//*[@id="root"]/main/div/div[2]/div[2]/button[2]'))  # יש לי חשבון
    actions.click_element(account_exist_button)
    phone_filed = actions.find_element((By.XPATH, '//*[@id="root"]/main/div/div[2]/div/form/input'))
    actions.send_keys(phone_filed, '0533363708')
    enter_button = actions.find_element((By.XPATH, '//*[@id="root"]/main/div/div[2]/div/form/button'))
    actions.click_element(enter_button)
    time.sleep(17)
    # wait for enter code
    submit_button = actions.find_element((By.XPATH, '//*[@id="root"]/main/div/div[2]/div/form/button'))
    actions.click_element(submit_button)



def is_soccer(category_text):
    if category_text == 'ספורט':
        pass


def is_theater(category_text):
    pass


def events_details(category_text, one_artist_bool, artist_name_text, event_date_text, event_time_text,
                    where_event_text):
    category_field = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.category_field)
    actions.send_keys(category_field, category_text)
    time.sleep(3)
    if one_artist_bool:
        num_of_artist = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.one_artist_radio_locator)
    else:
        num_of_artist = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.artist_radio_locator)
    num_of_artist.click()
    time.sleep(3)

    artist_name_field = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.artistName_field)
    actions.send_keys(artist_name_field, artist_name_text)
    time.sleep(3)
    event_date_field = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.eventDate_field)
    actions.send_keys(event_date_field, event_date_text)
    time.sleep(3)
    where_event_field = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.where_event_field)
    actions.send_keys(where_event_field, where_event_text)
    time.sleep(3)
    event_time_field = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.eventTime_field)
    actions.send_keys(event_time_field, event_time_text)
    time.sleep(3)
    next_button = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.next_button)
    actions.click_element(next_button)
    return (actions)


def event_style(sitting_details_text, ticket_type_text, ticket_quantity_text, ticket_price_text):
    sitting_details_field = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.sitting_details_field)
    actions.send_keys(sitting_details_field, sitting_details_text)

    ticket_type_field = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.ticket_type_field)
    actions.send_keys(ticket_type_field, ticket_type_text)

    ticket_quantity_field = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.ticket_quantity_field)
    actions.send_keys(ticket_quantity_field, ticket_quantity_text)

    ticket_price_field = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.ticket_price_field)
    actions.send_keys(ticket_price_field, ticket_price_text)

    # drv.find_element_by_id("IdOfInputTypeFile").send_keys(os.getcwd()+"/image.png")

    # upload_file = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.upload_file)
    # actions.send_keys(upload_file, os.getcwd()+"/image.png")

    next_button = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.next_button)
    actions.click_element(next_button)


def summary_page(full_name_text, bank_name_text, branch_number_text, account_number_text):
    actions = navigation_to_selling_tickets(my_driver)  # לא טוב

    full_name_field = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.full_name_field)
    actions.send_keys(full_name_field, full_name_text)

    bank_name_field = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.bank_name_field)
    actions.send_keys(bank_name_field, bank_name_text)

    branch_number_field = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.branch_number_field)
    actions.send_keys(branch_number_field, branch_number_text)

    account_number_field = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.account_number_field)
    actions.send_keys(account_number_field, account_number_text)

    terms_checkbox = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.terms_checkbox)
    terms_checkbox.click()
    # קראתי את תנאי השימוש


def success_page():
    back_to_home = actions.find_element(safsarX_selling_Tickets.data_of_elements.data.back_to_home)
    actions.click_element(back_to_home)


navigation_to_selling_tickets()
events_deatails('ילדים',True,'מאןר','03-02-2023','12:12','תל אביב')
time.sleep(5)
