from selenium.webdriver.common.by import By

# GENERAL
selling_tickets_button = (By.XPATH, '"//*[@id="root"]/div[1]/div/nav/p"')
next_button = (By.XPATH, '//*[@id="eventInfoForm"]/div[4]/button')


# - - - EVENT INFO [1/3] - - - #

    #UPPER [1/3]
category_name_field = (By.XPATH, '//*[@id="category"]/div/div/div/div/div/div/div/span[2]')
sports_type_name_field = (By.XPATH, '//*[@id="eventInfoForm_subCategory"]')
    #MIDDLE [2/3]
showtype_single_radio = (By.XPATH, '//*[@id="eventInfoForm_artistType"]/label[1]/span[1]/input')
showtype_multiple_radio = (By.XPATH, '//*[@id="eventInfoForm_artistType"]/label[2]/span[1]/input')
performer_name_field = (By.XPATH, '//*[@id="eventInfoForm_artistName"]')
performance_name_field = (By.XPATH, '//*[@id="eventInfoForm_eventName"]')
    #LOWER [3/3]
event_date_calendar = (By.XPATH, '//*[@id="eventInfoForm_eventDate"]/input')
event_date_range_checkbox = (By.XPATH, '//*[@id="eventInfoForm_eventDate"]/div/div[2]/div[1]/label/label/span/input')
event_location_field = (By.XPATH, '//*[@id="eventInfoForm_eventLocation"]')
event_time_field = (By.XPATH, '//*[@id="eventInfoForm_eventTime"]')

# Sport
which_branch_field = (By.ID, 'eventInfoForm_subCategory')
gametype_regular_radio = (By.XPATH, '//*[@id="eventInfoForm_gameType"]/label[1]/span[1]/input')
gametype_tournament_radio = (By.XPATH, '//*[@id="eventInfoForm_gameType"]/label[2]/span[1]/input')


# regular & tournament
game_name = (By.ID, 'eventInfoForm_gameName')
playing_team = (By.ID, 'eventInfoForm_playingTeam')
against_team = (By.ID, 'eventInfoForm_againstTeam')

# theater
eventName = (By.ID, 'eventInfoForm_eventName')


# second process in selling

back_button = (By.XPATH, "//button[text()='חזרה']")
next_button = (By.XPATH, "//button[text()='הבא']")

event_style = []

sitting_details_field = (By.ID, "eventInfoForm_typeDescription")
ticket_type_field = (By.ID, "eventInfoForm_ticketType")
ticket_quantity_field = (By.ID, "eventInfoForm_ticketQuantity")
ticket_price_field = (By.ID, "eventInfoForm_ticketPrice")

upload_file = ''

upload_button = (By.XPATH, "//button[text()='העלאת קובץ נוסף']")
delete_buttons = (By.XPATH, "//li/button")

# thread process in selling

back_button = (By.XPATH, "//button[text()='חזרה']")
next_button = (By.XPATH, "//button[text()='הבא']")

full_name_field = (By.ID, "eventInfoForm_fullName")
bank_name_field = (By.ID, "eventInfoForm_bankName")
branch_number_field = (By.ID, "eventInfoForm_branchNumber")
account_number_field = (By.ID, "eventInfoForm_accountNumber")

terms_checkbox = (By.XPATH, "//label[text()='קראתי והסכמתי ל']/preceding-sibling/input[@type='checkbox']")
email_updates_checkbox = (By.XPATH, "//label[text()='קבל עדכונים במייל']/preceding-sibling/input[@type='checkbox']")

# success_page
back_to_home = (By.XPATH, '//*[@id="root"]/main/div[2]/div/a')
succsess_text = (By.XPATH, '//*[@id="root"]/main/div[2]/div/p')
